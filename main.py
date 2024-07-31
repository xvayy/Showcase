import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo1.jpg")

with col2:
    st.title("Yuliia Ivaniuk")
    content = """Hi I am Yuliia! I am Pythin programmer. I study Computer Sience and try to do my best to find well-paid job"""
    st.info(content)