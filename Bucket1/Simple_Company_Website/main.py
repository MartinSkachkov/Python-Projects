import streamlit as st
import pandas


def handle_data(row):
    name = (row["first name"].strip() + ' ' + row["last name"].strip()).title()
    role = row["role"]
    image = "images/" + row["image"]
    st.subheader(name)
    st.write(role)
    st.image(image)


st.set_page_config(layout="wide")

st.title("Innovatech Solutions")
st.info("""Innovatech Solutions is a leading provider of cutting-edge technology solutions, dedicated to transforming businesses through 
innovation and excellence. Our team of experts specializes in delivering bespoke software development,
advanced data analytics, and cloud-based services to meet the unique needs of our clients.""")
st.header("Our Team")

df = pandas.read_csv("data.csv")

col1, col2, col3 = st.columns(3)

with col1:
    for idx, row in df[:4].iterrows():
        handle_data(row)

with col2:
    for idx, row in df[4:8].iterrows():
        handle_data(row)

with col3:
    for idx, row in df[8:].iterrows():
        handle_data(row)
