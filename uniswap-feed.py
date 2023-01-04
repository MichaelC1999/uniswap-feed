from substreams import Substream
from streamlit.runtime.scriptrunner.script_run_context import add_script_run_ctx, get_script_run_ctx

import streamlit as st
from tempfile import NamedTemporaryFile
import pandas as pd
import substreams as sub
import threading
import time
import requests
import math
import types




st.set_page_config(layout='wide')
sb = None
sb_keys = []

sb = Substream('./substreams-uniswap-v2-v0.1.1.spkg')

if bool(st.session_state) is False:
    st.session_state['streamed_data'] = []
    st.session_state['retruned_block_numbers'] = []
    st.session_state['highest_processed_block'] = 0    
    st.session_state['attempt_failures'] = 0
    st.session_state['error_message'] = None
    st.experimental_rerun()


# get eth chain head block from etherscan
if 'min_block' not in st.session_state:
    block_req_url = "https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp=" + str(math.ceil(time.time())) + "&closest=before&apikey=855E3F6RGATSRCBU3PSV2BW7G9UBPFQZKB"
    resp = requests.get(block_req_url)
    block_to_set = 11590000
    # if resp.status_code == 200:
    #     if math.isnan(int(resp.json()["result"])) is False:
    #         block_to_set = int(resp.json()["result"])-100
    # else:
    #     print('Request Error: {}: invalid token name'.format(resp.status_code))
    st.session_state['min_block'] = block_to_set
    

min_block = st.session_state['min_block']
max_block = 20000000

if 'streamed_data' in st.session_state:
    if len(st.session_state['streamed_data']) > 0:
        copy_df = pd.DataFrame(st.session_state['streamed_data'])
        if list(copy_df.columns):
            st.selectbox("Select Substream Table Sort Column", options=list(copy_df.columns), key="rank_col") 

        if st.session_state['rank_col'] is not None:
            copy_df = copy_df.sort_values(by=st.session_state['rank_col'],ascending=False)
            copy_df.index = range(1, len(copy_df) + 1)
            copy_df['txHash'] = '0x' + copy_df['txHash'].astype(str)
            copy_df['poolAddress'] = '0x' + copy_df['poolAddress'].astype(str)
            copy_df['sender'] = '0x' + copy_df['sender'].astype(str)
        html_table = '<div class="table-container">' + copy_df[:500].to_html() + '</div>'
        style_css = """
                <style>
                    div.table-container {
                        width: 100%;
                        overflow: scroll;
                    }

                    table.dataframe {
                    width: 100%;
                    background-color: rgb(35,58,79);
                    border-collapse: collapse;
                    border-width: 2px;
                    border-color: rgb(17,29,40);
                    border-style: solid;
                    color: white;
                    font-size: 14px;
                    }

                    table.dataframe td, table.dataframe th {
                    text-align: left;
                    border-top: 2px rgb(17,29,40) solid;
                    border-bottom: 2px rgb(17,29,40) solid;
                    padding: 3px;
                    white-space:nowrap;
                    }

                    table.dataframe thead {
                        color: rgb(215,215,215);
                    background-color: rgb(17,29,40);
                    }
                </style>"""
        st.markdown(style_css + html_table, unsafe_allow_html=True)

if sb is not None:
    init_block = sb.output_modules["store_swap_events"]["initial_block"]
    total_blocks = st.session_state['min_block'] - init_block
    blocks_processed = st.session_state['highest_processed_block'] - init_block
    if init_block > 0 and total_blocks > 0 and blocks_processed > 0:
        st.write('Estimated progress: ' + str(math.ceil(100*blocks_processed/total_blocks)) + '% ' + 'Initial Block: ' + str(init_block) + ' Highest Processed Block: ' + str(st.session_state['highest_processed_block']) + ' Start Block: ' + str(st.session_state['min_block']))

if st.session_state['error_message'] is not None:
    st.write("ERROR:" + st.session_state['error_message'])

if "min_block" in st.session_state:
    min_block = st.session_state["min_block"]
    if min_block > 0:
        if max_block < min_block:
            max_block = 20000000
        if max_block == min_block:
            st.session_state["min_block"] = 0
        if max_block > min_block and sb is not None:
            module_name = "store_swap_events"
            poll_return_obj = {}
            try:
                print('BEFO', min_block, st.session_state['highest_processed_block'])
                poll_return_obj = sb.poll([module_name], start_block=min_block, end_block=max_block, return_first_result=True, highest_processed_block=st.session_state['highest_processed_block'], return_progress=True)
                if 'error' in poll_return_obj:
                    raise TypeError(poll_return_obj["error"].debug_error_string() + ' BLOCK: ' + poll_return_obj["data_block"])
            except Exception as e:
                print("ERROR --- TRY AGAIN ", e)
                attempt_failures = st.session_state['attempt_failures']
                attempt_failures += 1
                if attempt_failures % 10 == 0:
                    st.session_state["min_block"] = max_block
                    st.session_state['error_message'] = "Maximum attempts reached. Substream returned RST error " + str(attempt_failures) + " times." 
                else:
                    st.session_state["min_block"] = min_block - 4900
                st.session_state['attempt_failures'] = attempt_failures

            # print(min_block, st.session_state['highest_processed_block'], poll_return_obj.keys(), 'st.session')
            if "block" in poll_return_obj:
                st.session_state['highest_processed_block'] = poll_return_obj["block"]
                
            elif "data" in poll_return_obj:
                if (len(poll_return_obj["data"]) > 0) and poll_return_obj["data_block"] not in st.session_state['retruned_block_numbers']:
                    st.session_state['streamed_data'].extend(poll_return_obj["data"])
                    st.session_state['retruned_block_numbers'].append(poll_return_obj["data_block"])
                    print('RETURNING DATA - MIN BLOCK:', min_block, ' POLLING RETURNED BLOCK:', poll_return_obj["data_block"], ' HIGHEST BLOCK(BEFORE UPDATE):', st.session_state['highest_processed_block'])
                if int(poll_return_obj["data_block"]) > st.session_state['highest_processed_block']:
                    st.session_state['highest_processed_block'] = int(poll_return_obj["data_block"])


                st.session_state['min_block'] = int(poll_return_obj["data_block"]) + 4900
            print(min_block, st.session_state['min_block'], st.session_state['highest_processed_block'], poll_return_obj.keys(), 'AFT LOG')
            st.experimental_rerun()
