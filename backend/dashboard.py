'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-06-05 11:41:36
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-06-05 12:16:57
FilePath: /NTTU-new-gen-judge-system/backend/dashboard.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import streamlit as st
import time
import psutil

def get_cpu_info():
    return psutil.cpu_percent(interval=1, percpu=True)

def get_memory_info():
    return psutil.virtual_memory().percent

def get_disk_info():
    return psutil.disk_usage('/').percent

def main_page():
    st.title("NTTU Judge System Dashboard")
    if st.button("Refresh"):
        st.experimental_rerun()
    cpu , memory, disk = st.tabs(["CPU", "Memory", "Disk"])
    with cpu:
        col1 ,  col2, col3 = st.columns(3)
        cpu_list = get_cpu_info()
        for i in range(len(cpu_list)):
            pos = i%3
            if pos == 2:
                col3.metric(label=f"CPU {i}", value=f"{cpu_list[i]}%")
            elif pos == 1:
                col2.metric(label=f"CPU {i}", value=f"{cpu_list[i]}%")
            else:
                col1.metric(label=f"CPU {i}", value=f"{cpu_list[i]}%")
    with memory:
        st.metric(label="Memory", value=f"{get_memory_info()}%")
    with disk:
        st.metric(label="Disk", value=f"{get_disk_info()}%")

def database_page():
    st.title("Database")
    st.write("This is the database page")

pages = {
    "Main": main_page,
    "Database": database_page
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))
pages[selection]()