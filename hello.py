import streamlit as st

st.header("This is  My first web app")


code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")



agree = st.checkbox("I'm learning about Steramlit ")
if agree:
    st.write("Great!")
