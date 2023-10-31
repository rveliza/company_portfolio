import streamlit as st


with st.form(key="email_forms"):

    user_email = st.text_input("Your Email Address")

    user_topic = st.selectbox("What topics do you want to discuss?", 
                             ["Job Proposals", "Job Inquiries", "Other"])
    
    user_text = st.text_area("Text")

    message = f"""\
Subject: New email from {user_email}
From {user_email}
Topic {user_topic}
{user_text}
"""

    button = st.form_submit_button("Submit!")

    if button:
        st.info("Your email was sent succesfully")
        st.write(message)