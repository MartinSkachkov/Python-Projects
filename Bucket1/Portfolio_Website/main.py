import streamlit as st

st.set_page_config(layout="wide")

# col1: for the profile pic
# col2: for the "About me"
col1, col2 = st.columns(2)

with col1:
    st.image("images/profile.jpg")

with col2:
    st.title("Martin Skachkov")
    content = """
              I am currently in my third year studying Computer Science at the Faculty of Mathematics and Informatics at Sofia University St. Kliment Ohridski. I am highly motivated and passionate about exploring the details of computer science, eager to learn more about both theoretical concepts and practical applications. My academic journey has been challenging and rewarding, and I look forward to improving my skills and contributing to the field of technology.
              """
    st.info(content)
