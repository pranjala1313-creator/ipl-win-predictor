import pandas as pd
import streamlit as st
import pickle
import os

st.title("IPL Win Predictor")

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
]

teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals'
]

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'pipe.pkl'), 'rb') as file:
    pipe = pickle.load(file)

# Team selection
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox(
        'Select the batting team',
        teams
    )

with col2:
    bowling_team = st.selectbox(
        'Select the bowling team',
        teams
    )

# City
select_city = st.selectbox(
    "Select host city",
    cities
)

# Target
target = st.number_input("Enter Target score")

# Match information
col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input("Enter Score")

with col4:
    overs = st.number_input("Enter Overs completed")

with col5:
    wicket = st.number_input("Enter Wickets out")

if st.button("Predict"):

    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wicket

    if overs > 0:
        crr = score / overs
    else:
        crr = 0

    if balls_left > 0:
        rrr = runs_left * 6 / balls_left
    else:
        rrr = 0

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [select_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    st.table(input_df)

    result = pipe.predict_proba(input_df)

    st.subheader(f"Winning probablity of {bowling_team}-{round(result[0][0]*100)}%")
    st.subheader(f"Winning probablity of {batting_team}-{round(result[0][1]*100)}%")