import streamlit as st

st.title("Chai Maker app")

if st.button("Make Chai"):
    st.success("Your chai is being brewed")

add_masala=st.checkbox("Add masala")

if add_masala:
    st.success("Masala added to your chai")


tea_type=st.radio("Pick your base",
                  ["Milk","Water","Oat Milk"])

if tea_type:
    st.write(f"you selected {tea_type} as your base")

flavour=st.selectbox("Select your flavour",
                        ["Adrak","kesar","Tulsi"])

st.write(f"you selected {flavour} as your flavour")

sugar=st.slider("select sugar level",0,5,2)

st.write(f"Sugar level is {sugar}")

cup=st.number_input("How many cups", min_value=1, max_value=5, step=1)
st.write(f"You selected {cup} cups")

name=st.text_input("What is your name")

if name:
    st.write(f"Hello {name} your chai is ready!")\

dob=st.date_input("What is your date of birth")
if dob:
    st.write(f"Your date of birth is {dob}")