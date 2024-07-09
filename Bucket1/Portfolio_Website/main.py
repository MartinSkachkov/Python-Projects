import streamlit as st
import pandas


def display_column(row):
    st.header(row["title"])
    st.write(row["description"])
    st.image(f"images/{row['image']}")
    st.write(f"[Source Code]({row['url']})")


st.set_page_config(layout="centered")

profile_column, about_me = st.columns(2)

with profile_column:
    st.write("")  # needed for top spacing
    image_path = "images/profile.jpg"
    st.markdown(f'<style>div.stImage > img {{ margin-top: 300px; }}</style>', unsafe_allow_html=True)
    st.image(image_path, width=350)

with about_me:
    st.header("Martin Skachkov")
    content = """
              Hi, I am Martin!
              I am currently in my third year, studying Computer Science at the Faculty of Mathematics 
              and Informatics at Sofia University St. Kliment Ohridski. I am highly motivated and passionate
              about exploring the details of computer science, eager to learn more about both theoretical 
              concepts and practical applications. My academic journey has been challenging and rewarding,
               and I look forward to improving my skills and contributing to the field of technology.
              """
    st.info(content)

st.write("""
Below you can find some of the apps I have built in Python:
""")

# implementing the projects display
projects_col1, empty_col, projects_col2 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with projects_col1:
    for idx, row in df[:10].iterrows():
        display_column(row)

with projects_col2:
    for idx, row in df[10:].iterrows():
        display_column(row)
