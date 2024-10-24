import streamlit as st

def Login():
    with st.form(key='login_form'):
        st.write("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        submit = st.form_submit_button("Login")
        if submit:
            st.session_state.username = username
            st.session_state.password = password