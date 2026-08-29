import streamlit as st
import requests
st.title("live currency convereter")
amount=st.number_input("enter the currency amount",min_value=1)
target_currency=st.selectbox("Select the currency",["USD","EUR","GBP","JPY"])

if st.button("Convert"):
    url="https://api.exchangerate-api.com/v4/latest/INR"
    response=requests.get(url)

    if response.status_code==200:
        data=response.json()
        rate=data["rates"][target_currency]
        converted_amount=amount*rate
        st.success(f"Your converted amount is: {converted_amount} {target_currency}")
    else:
        st.error("Failed to fetch conversion rate")