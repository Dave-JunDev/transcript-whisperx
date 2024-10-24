import streamlit as st
from services.chat import conversation

def Chat():
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    st.title("💬 Chatbot")
    prompt = st.chat_input("Hello, what's your name?")
    st.button("Restart conversation", on_click=clear_conversation)
    if prompt:
        st.session_state.messages.append({"role" : "human", "content" : prompt})
        answer = conversation(st.session_state.messages)
        st.session_state.messages.append({"role" : "assistant", "content" : answer})
        print(st.session_state.messages)

    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.write(message['content'])

        
def clear_conversation():
    st.session_state.messages = []

        
    
       
