import streamlit as st
from views.login import Login
from views.video import Video
from views.chat import Chat

pages = {
    "Login" : [
        st.Page(Login, title="Login")
    ],
    "Video IA" : [
        st.Page(Video, title="Video transcript")
    ],
    "Chat IA" : [
        st.Page(Chat, title="Chat transcript")
    ]
}

def main():
    pg = st.navigation(pages)
    pg.run()
