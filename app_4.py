import streamlit as st
import pandas as pd

st.title("Chai Sales Dashboard")

file=st.file_uploader("Upload your csv file here",type=["csv"])


if file:
    df=pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())


if file:
    Cities=df['City'].unique()
    st.subheader("Cities")
    selected_city=st.selectbox("Select City",Cities)
    st.write(df[df['City']==selected_city])