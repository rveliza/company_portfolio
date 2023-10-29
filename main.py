import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

st.set_page_config(layout="wide")



st.header("The Best Company")


contet = "iatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt"

st.write(contet)

st.subheader("Our Team")

col1, empty_col1, col2, empty_col2, col3 = st.columns([1.5, .5, 1.5, .5, 1.5])

with col1:
    for index, row in df[:4].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.subheader(row["role"])
        st.image("images/" + row["image"])


with col2:
    for index, row in df[4:8].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.subheader(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.subheader(row["role"])
        st.image("images/" + row["image"])

