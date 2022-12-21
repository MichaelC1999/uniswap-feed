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

if 'streamed_data' not in st.session_state:
    st.session_state['streamed_data'] = []
if 'highest_processed_block' not in st.session_state:
    st.session_state['highest_processed_block'] = 0    

# get eth chain head block from etherscan
if 'min_block' not in st.session_state:
    block_req_url = "https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp=" + str(math.ceil(time.time())) + "&closest=before&apikey=855E3F6RGATSRCBU3PSV2BW7G9UBPFQZKB"
    resp = requests.get(block_req_url)
    block_to_set = 16000000
    if resp.status_code == 200:
        if math.isnan(int(resp.json()["result"])) is False:
            block_to_set = int(resp.json()["result"])
    else:
        print('Request Error: {}: invalid token name'.format(resp.status_code))
    st.session_state['min_block'] = block_to_set
    

min_block = st.session_state['min_block']
print(min_block, 'minnnn')
max_block = 20000000

if 'streamed_data' in st.session_state:
    if len(st.session_state['streamed_data']) > 0:
        copy_df = pd.DataFrame(st.session_state['streamed_data'])
        print(copy_df, st.session_state['streamed_data'])
        if list(copy_df.columns):
            st.selectbox("Select Substream Table Sort Column", options=list(copy_df.columns), key="rank_col") 

        if st.session_state['rank_col'] is not None:
            copy_df = copy_df.sort_values(by=st.session_state['rank_col'],ascending=False)
            copy_df.index = range(1, len(copy_df) + 1)
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
    remaining_blocks = st.session_state['min_block'] - st.session_state['highest_processed_block']
    st.write('Estimated progress: ' + str(math.ceil(100*remaining_blocks/total_blocks)) + '% ' + str(st.session_state['highest_processed_block']) + '/' + str(st.session_state['min_block']))



if "min_block" in st.session_state:
    min_block = st.session_state["min_block"]
    print(max_block, type(max_block), min_block, type(min_block), 'running substream')
    if min_block > 0:
        if max_block < min_block:
            max_block = 20000000
        if max_block == min_block:
            st.session_state["min_block"] = 0
        if max_block > min_block and sb is not None:
            module_name = "store_swap_events"
            rec = sb.poll_return_first_dict([module_name], start_block=min_block, end_block=max_block, highest_processed_block=st.session_state['highest_processed_block'])
            print(str(rec), 'rec', type((rec)))
            if "block" in rec:
                st.session_state['highest_processed_block'] = rec["block"]
                
            elif "data" in rec:
                if (len(rec["data"]) > 0):
                    st.session_state['streamed_data'].extend(rec["data"])
                
                st.session_state['min_block'] = int(rec["min_block"]) + 1
            print(st.session_state, "state")
            st.experimental_rerun()
