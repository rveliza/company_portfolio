import streamlit as st
from send_emails import send_email
import pandas

df = pandas.read_csv("topics.csv")


with st.form(key="email_forms"):

    user_email = st.text_input("Your Email Address")

    user_topic = st.selectbox("What topics do you want to discuss?", 
                             df["topic"])
    
    user_text = st.text_area("Text")

    message = f"""\
Subject: New email from {user_email}
From {user_email}
Topic {user_topic}
{user_text}
"""

    button = st.form_submit_button("Submit!")

    if button:
        send_email(message)
        st.info("Your email was sent succesfully")
