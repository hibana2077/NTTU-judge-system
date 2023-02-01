import requests
import yaml
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
import pandas as pd

ADMIN_LIST = ["admin","Admin","ADMIN"]

with open("frontend/config.yaml", "r") as f:config = yaml.load(f, Loader=yaml.SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login('Login', 'sidebar')
if authentication_status:
    authenticator.logout('Logout', 'sidebar')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

# elif st.session_state.switch_button != switch_button:

# hashed_passwords = stauth.Hasher(['admin']).generate()
# print(hashed_passwords)

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

def streamlit_menu():
    with st.sidebar:
            selected = option_menu(
                menu_title="選單",  # required
                options=["Home", "Problem", "Contest"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="list",  # optional
                default_index=0,  # optional
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
    if case == "Teacher":
        with st.sidebar:
            selected = option_menu(
                menu_title="管理者選單",  # required
                options=["Home", "Contest setting"],  # required
                icons=["house", "book"],  # optional
                menu_icon="list",  # optional
                default_index=0,  # optional
            )
        return selected
    else:
        with st.sidebar:
            selected = option_menu(
                menu_title="訪客選單",  # required
                options=["Home", "Score board"],  # required
                icons=["house", "bar-chart-line"],  # optional
                menu_icon="list",  # optional
                default_index=0
            )
        return selected


#留以下的dict
ADMIN_PAGES = {
    "Home": home,
    "Contest setting": contest_setting
}

STUDENT_PAGES  = {
    "Home": home,
    "Problem": problem,
    "Contest": contest
}

CUSTOMER_PAGES = {
    "Home": home,
    "Score board": rank
}

if st.session_state.name in ADMIN_LIST:
    page = ADMIN_PAGES[streamlit_menu_switch("Teacher")]
elif st.session_state.name != None:
    page = STUDENT_PAGES[streamlit_menu_switch("Student")]
else:
    page = CUSTOMER_PAGES[streamlit_menu_switch("Visitor")]
page()
# print(st.session_state)