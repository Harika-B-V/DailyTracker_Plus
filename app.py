import streamlit as st
import openpyxl
from datetime import date

import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe

id = '1iwGL8NBwH1BONg8i6DO4ReURIzL720ZL44jHYgrmzfg'

gc = gspread.service_account(filename='dailytracker_plus.json')
sh = gc.open_by_key(id)
worksheet = sh.get_worksheet(0)

#Date
today = date.today()

# UI for the page
st.markdown("<h1 style='text-align: center; color: black;'>Daily Tracker ++</h1>", unsafe_allow_html=True)


def save_in_daily_tracker(sessions, learnings, project_tasks):
    
    dataframe = pd.DataFrame(worksheet.get_all_records())
    max_row = len(dataframe.index)

    data = [[today], [sessions], [learnings], [project_tasks]]

    df = pd.DataFrame(data)
    df = df.T
    df.reset_index(drop=True, inplace=True)
    set_with_dataframe(worksheet, df, row=max_row+1, col=1, include_column_header=False, include_index=False)


sessions = st.text_area("Tell about the sessions you attended today", "Type Here ...")
learnings = st.text_area("Tell about the learnings for the day", "Type Here ...")
project_tasks = st.text_area("Tell about your project related tasks", "Type Here ...")


if(st.button('Submit')):
    save_in_daily_tracker(sessions.title(), learnings.title(), project_tasks.title())
    st.success("Hurray! Saved successfully")
    st.balloons()
