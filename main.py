import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo1.jpg")

with col2:
    st.title("Yuliia Ivaniuk")
    content = """Hi I am Yuliia! I am Pythin programmer. I study Computer Sience and try to do my best to find well-paid job"""
    st.info(content)

content2 = """"Below you can find some of the apps I have build in Python. Feel free to contact me!"""
st.write(content2)

col3, col4 = st.columns(2)

data_frame = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in data_frame[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row["image"]}")
        st.link_button(label="Link to the project", url=row["url"])



with col4:
    for index, row in data_frame[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row["image"]}")
        st.link_button(label="Link to the project", url=row["url"])