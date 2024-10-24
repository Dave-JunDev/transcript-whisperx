import streamlit as st
from views.login import Login
from views.video import Video

pages = {
    "Login" : [
        st.Page(Login, title="Login")
    ],
    "Video IA" : [
        st.Page(Video, title="Video transcript")
    ]
}

def main():
    pg = st.navigation(pages)
    pg.run()
