import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email adress")
    my_message = st.text_area("Your message")
    letter = f"""\
Subject: Meeting
{my_message}
From {user_email}
"""
    button = st.form_submit_button()
    if button:
        send_email(letter)
        st.info("Your email was send succesfully")

#oxno eybz nwdc bezz