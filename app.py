import streamlit as st

st.title("My first project")
name = st.text_input("What is your name?")
st.write(f"Здравей, {name}")
