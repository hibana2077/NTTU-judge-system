'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-01-16 22:12:07
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-01-26 15:32:42
FilePath: /NTTU-new-gen-judge-system/frontend/client.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests
import yaml
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
import pandas as pd

switch_button = st.sidebar.radio(
        "Teacher or Student?",
        ("Teacher", "Student")
    )

with open("frontend/config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.SafeLoader)

# hashed_passwords = stauth.Hasher('admin').generate()
# print(hashed_passwords)

def login():
    pass

def home():
    st.title("NTTU Online Judge")

def problem():
    st.write("Problem")

def contest():
    st.write("Contest")

def rank():
    st.write("Rank")

def profile():
    st.write("Profile")

def contest_setting():
    st.write("Contest setting")

# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )


# name, authentication_status, username = authenticator.login('Login', 'main')

# if authentication_status:
#     authenticator.logout('Logout', 'main')
#     st.write(f'Welcome *{name}*')
#     st.title('Some content')
# elif authentication_status == False:
#     st.error('Username/password is incorrect')
# elif authentication_status == None:
#     st.warning('Please enter your username and password')


def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="選單",  # required
                options=["Home", "Problem", "Contest"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="list",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title="None",  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="list",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected
    
def streamlit_menu_switch(case="Student"):
    if case == "Student":
        with st.sidebar:
            selected = option_menu(
                menu_title="學生選單",  # required
                options=["Home", "Problem", "Contest"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="list",  # optional
                default_index=0,  # optional
            )
        return selected
    else:
        with st.sidebar:
            selected = option_menu(
                menu_title="管理者選單",  # required
                options=["Home", "Contest setting"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="list",  # optional
                default_index=0,  # optional
            )
        return selected

PAGES = {
    "Home": home,
    "Problem": problem,
    "Contest": contest,
    "Rank": rank,
    "Profile": profile
}

PAGES_TEACHER = {
    "Home": home,
    "Contest setting": contest_setting,
}

page = PAGES[streamlit_menu_switch(switch_button)] if switch_button == "Student" else PAGES_TEACHER[streamlit_menu_switch(switch_button)]
page()