from substreams import Substream
from streamlit.runtime.scriptrunner.script_run_context import add_script_run_ctx, get_script_run_ctx

import streamlit as st
from tempfile import NamedTemporaryFile
import pandas as pd
import substreams as sub
import os
import threading
import time
import requests
import math
import types

from dotenv import load_dotenv
load_dotenv()


st.set_page_config(layout='wide')
sb = None
sb_keys = []


if bool(st.session_state) is False:
    st.session_state['streamed_data'] = []
    st.session_state['retruned_block_numbers'] = []
    st.session_state['highest_processed_block'] = 0    
    st.session_state['attempt_failures'] = 0
    st.session_state['error_message'] = ""
    st.session_state['has_started'] = False
    st.session_state["sftoken"] = None
    st.experimental_rerun()

block_start = st.number_input('START BLOCK:', min_value=10000835, max_value=20000001)

stop_message = st.empty()
if 'has_started' in st.session_state:
    if st.session_state['has_started'] is False:
        execute_button = st.button('Start Execution')
        if execute_button is True:
            st.session_state["min_block"] = block_start
            st.session_state['has_started'] = True
            st.experimental_rerun()
    if st.session_state['has_started'] is True:
        execute_button = st.button('Stop Execution')
        if execute_button is True:
            stop_message.write('Stopping...')
            st.session_state['has_started'] = False
            st.experimental_rerun()


if "SUBSTREAMS_API_TOKEN" in os.environ:
    st.session_state["sftoken"] = os.environ["SUBSTREAMS_API_TOKEN"]
elif "APIKEY" in os.environ and st.session_state["sftoken"] is None:
    APIKEY = os.environ["APIKEY"]
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = '{"api_key": "' + APIKEY + '"}'
    response = requests.post('https://auth.streamingfast.io/v1/auth/issue', headers=headers, data=data)
    resp_json = response.json()
    if "token" in resp_json:
        st.session_state["sftoken"] = resp_json["token"]

sb = Substream('./substreams-uniswap-v2-v0.1.1.spkg', token=st.session_state["sftoken"])
# get eth chain head block from etherscan
# if 'min_block' not in st.session_state and 'block_to_start' in st.session_state:
    # While in development, no need to use chain head. Temporarily commenting out
    # block_req_url = "https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp=" + str(math.ceil(time.time())) + "&closest=before&apikey=855E3F6RGATSRCBU3PSV2BW7G9UBPFQZKB"
    # resp = requests.get(block_req_url)
    # block_to_set = st.session_state['block_to_start']
    
    # if resp.status_code == 200:
    #     if math.isnan(int(resp.json()["result"])) is False:
    #         block_to_set = int(resp.json()["result"])-100
    # else:
    #     print('Request Error: {}: invalid token name'.format(resp.status_code))
    # st.session_state['min_block'] = block_to_set
    
min_block = 10000835
if 'min_block' in st.session_state:
    min_block = st.session_state['min_block']
    
max_block = 20000000

placeholder = st.empty()

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

error_message = st.empty()

if 'error_message' in st.session_state:
    if st.session_state['error_message'] != "" and st.session_state['error_message'] is not None: 
        error_message.text(st.session_state['error_message'])

if st.session_state['has_started'] is True:
    st.session_state['error_message'] = ""
    if 'min_block' in st.session_state:
        # If min_block is saved in state, override the min_block from the UI input
        min_block = st.session_state['min_block']
    if min_block > 0:
        if max_block < min_block:
            raise TypeError('`min_block` is greater than `max_block`. This cannot be validly polled.')
        if max_block == min_block:
            st.session_state["min_block"] = 0
            st.session_state['has_started'] = False
            st.experimental_rerun()
        if max_block > min_block and sb is not None:
            poll_return_obj = {}
            try:
                placeholder.text("Loading Substream Results...")
                poll_return_obj = sb.poll(["map_swap_events"], start_block=min_block, end_block=max_block, return_first_result=True)
                placeholder.empty()
                if 'error' in poll_return_obj:
                    if "debug_error_string" in dir(poll_return_obj["error"]):
                        raise TypeError(poll_return_obj["error"].debug_error_string() + ' BLOCK: ' + poll_return_obj["data_block"])
                    else:
                        raise TypeError(str(poll_return_obj["error"]) + ' BLOCK: ' + poll_return_obj["data_block"])
                elif "data" in poll_return_obj:
                    if (len(poll_return_obj["data"]) > 0):
                        st.session_state['streamed_data'].extend(poll_return_obj["data"])
                    st.session_state['min_block'] = int(poll_return_obj["data_block"]) + 1
            except Exception as err:
                print("ERROR --- ", err)
                attempt_failures = st.session_state['attempt_failures']
                attempt_failures += 1
                if attempt_failures % 10 == 0:
                    st.session_state['error_message'] = "ERROR --- " + str(err)
                    st.session_state['has_started'] = False
                    st.session_state["min_block"] = max_block
                st.session_state['attempt_failures'] = attempt_failures
            st.experimental_rerun()
elif 'streamed_data' in st.session_state:
    if len(st.session_state['streamed_data']) > 0:
        st.write('Substream Polling Completed') 