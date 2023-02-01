import requests
import yaml
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
import pandas as pd

switch_button = st.sidebar.radio(
        "User mode",
        ("Teacher", "Student")
    )
if 'switch_button' not in st.session_state:
    st.session_state.switch_button = switch_button
# elif st.session_state.switch_button != switch_button:

# hashed_passwords = stauth.Hasher(['admin']).generate()
# print(hashed_passwords)

def login(mode:str):
    with open("frontend/config.yaml", "r") as f:config = yaml.load(f, Loader=yaml.SafeLoader)
    authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


    name, authentication_status, username = authenticator.login('Login', 'main')

    if authentication_status:
        authenticator.logout('Logout', 'sidebar')
        st.write(f'Welcome *{name}*')
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')

    return name, authentication_status, username

def home(mode:str):
    st.title("NTTU Online Judge")

def problem(mode:str):
    st.write("Problem")

def contest(mode:str):
    st.write("Contest")

def rank(mode:str):
    st.write("Rank")

def profile(mode:str):
    st.write("Profile")

def contest_setting(mode:str):
    st.write("Contest setting")

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
                options=["Home", "Problem", "Contest","Login"],  # required
                icons=["house", "book", "envelope","box-arrow-in-right"],  # optional
                menu_icon="list",  # optional
                default_index=0,  # optional
            )
        return selected
    if case == "Teacher":
        with st.sidebar:
            selected = option_menu(
                menu_title="管理者選單",  # required
                options=["Home", "Contest setting","Login"],  # required
                icons=["house", "book","box-arrow-in-right"],  # optional
                menu_icon="list",  # optional
                default_index=0,  # optional
            )
        return selected
    else:
        with st.sidebar:
            selected = option_menu(
                menu_title="預設選單",  # required
                options=["Home", "Problem", "Contest","Login"],  # required
                icons=["house", "book", "envelope","box-arrow-in-right"],  # optional
                menu_icon="list",  # optional
                default_index=0
            )
        return selected

PAGES = {
    "Home": home,
    "Problem": problem,
    "Contest": contest,
    "Rank": rank,
    "Profile": profile,
    "Login": login
}

PAGES_TEACHER = {
    "Home": home,
    "Contest setting": contest_setting,
    "Login": login
}

ADMIN_PAGES = {
    "Home": home,
    "Contest setting": contest_setting,
}

STUDENT_PAGES  = {
    "Home": home,
    "Problem": problem,
    "Contest": contest,
}

page = PAGES[streamlit_menu_switch(st.session_state.switch_button)] if st.session_state.switch_button else PAGES_TEACHER[streamlit_menu_switch(st.session_state.switch_button)]
page(st.session_state.switch_button)
# print(st.session_state)