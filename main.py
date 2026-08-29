import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello {name}!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
