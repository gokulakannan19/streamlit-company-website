import streamlit as st
import pandas as pd
from send_email import send_email

st.header("Contact Us")

df = pd.read_csv("topics.csv")
topic_list = list(df['topic'])

with st.form(key="email_form"):
    user_input = st.text_input("Your Email Address")
    topic = st.selectbox("Select a topic", topic_list)
    raw_message = st.text_area("Text Here...")

    message = f"""\
Subject: Company Website

Topic: {topic}
{raw_message}

Thank you
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Email send successfully")
