# Import necessary libraries
import streamlit as st
import pandas as pd
import random

# Load the idioms data (assuming 'idioms.csv' is in the same directory)
data = pd.read_csv('english_idioms.csv')
idioms = data[['idioms', 'meaning']].to_dict('records')

# Function to get a random idiom
def get_random_idiom():
    return random.choice(idioms)

# Streamlit app
st.title('Random English Idiom')

if st.button('Show a Random Idiom'):
    random_idiom = get_random_idiom()
    st.write(f"**Phrase:** {random_idiom['idioms']}")
    st.write(f"**Definition:** {random_idiom['meaning']}")

# To run the app, use the command: streamlit run app.py
