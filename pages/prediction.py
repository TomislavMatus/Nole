
from curses.ascii import alt
from urllib.error import URLError
import streamlit as st
import pandas as pd
import numpy as np
import pickle

number = st.number_input('Please enter your height in cm')
columns = st.columns(2)
ft = columns[0].number_input(label='Or, alternatively, Insert your height in feet',value=1, \
    min_value=0, max_value=50, step=1)
inch = columns[1].number_input(label='and inches',value=1, \
    min_value=0, max_value=50, step=1)
height = 0
if number > 0:
    height = number
    st.write(f'Your height in cm is {number} cm')
else:
    height = round((ft * 30.48) + (inch * 2.54))
    st.write(f'Your Height in cm is  {round((ft * 30.48) + (inch * 2.54))} cm')


age = st.number_input('Please enter your age in years',value=20, \
    min_value=0, max_value=9001, step=1)
st.write(f"Your age, in seconds, is {age*365*24*60*60} s. (In case you're interested.)")


surface_options = ['Hard','Clay','Carpet','Grass']
surface = st.selectbox(label='Please pick a surface', options=surface_options,\
     index=0,\
)
best_of_options = [3,5]
best_of = st.selectbox(label='Please pick the maximum number of sets',\
     options=best_of_options,\
     index=0,\
)
min_time =0
if best_of == 3:
    min_time=18
else:
    min_time = 36

match_time = st.number_input("How much time do you need to beat him?" ,value=min_time, \
    min_value=min_time, max_value=999999, step=1)
hand_options = ['Left','Right']
hand = st.selectbox(label='Left or Right handed?',\
     options=hand_options,\
     index=0,\
)
aces = st.number_input("Total number of Aces" ,value=0, \
    min_value=0, max_value=999999, step=1)

serve_points = st.number_input("Total number of Service Points" ,value=0, \
    min_value=0, max_value=999999, step=1)

first_in = st.number_input("First serves in" ,value=0, \
    min_value=0, max_value=999999, step=1)

first_won = st.number_input("First serves won" ,value=0, \
    min_value=0, max_value=999999, step=1)

second_won = st.number_input("Second serves won" ,value=0, \
    min_value=0, max_value=999999, step=1)

breaks_faced = st.number_input("Break points faced" ,value=0, \
    min_value=0, max_value=999999, step=1)

breaks_won = st.number_input("Break points won" ,value=0, \
    min_value=0, max_value=999999, step=1)

#Model 
loaded_model = pickle.load(open(filename, 'rb'))
