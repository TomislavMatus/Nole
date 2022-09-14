
from curses.ascii import alt
from urllib.error import URLError
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from pages.model import load_model
from pages.utils import surface_to_pred

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
#OHE - 3 =0, 5 = 1
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
#left-hand is 1 and rh is 0
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

double_faults = st.number_input("Number of Double Faults" ,value=0, \
    min_value=0, max_value=999999, step=1)


breaks_faced = st.number_input("Break points faced" ,value=0, \
    min_value=0, max_value=999999, step=1)

breaks_save = st.number_input("Break points won" ,value=0, \
    min_value=0, max_value=999999, step=1)


model = load_model('model.pickle')
#Note, has been scaled on user_input and would be nice to scale on X_train instead

# ['Hard', 'Clay', 'Carpet', 'Grass', 'best_of', 'minutes', 'opp_hand',
#        'opp_ht', 'opp_age', 'opp_ace', 'opp_df', 'opp_svpt', 'opp_1stIn',
#        'opp_1stWon', 'opp_2ndWon', 'opp_bpSaved', 'opp_bpFaced']

# pred_df = pd.DataFrame(columns=['Hard', 'Clay', 'Carpet', 'Grass', 'best_of', 'minutes', 'opp_hand',
#        'opp_ht', 'opp_age', 'opp_ace', 'opp_df', 'opp_svpt', 'opp_1stIn',
#        'opp_1stWon', 'opp_2ndWon', 'opp_bpSaved', 'opp_bpFaced'])


pred_df = pd.DataFrame()
pred_df

#pred_df = surface_to_pred(surface, pred_df)
if surface == 'Hard':
    pred_df.loc[0, 'Hard'] = 1
else:
    pred_df.loc[0, 'Hard'] = 0

if surface == 'Clay':
    pred_df.loc[0, 'Clay'] = 1
else:
    pred_df.loc[0, 'Clay'] = 0

if surface == 'Carpet':
    pred_df.loc[0, 'Carpet'] = 1
else:
    pred_df.loc[0, 'Carpet'] = 0

if surface == 'Grass':
    pred_df.loc[0, 'Grass'] = 1
else:
    pred_df.loc[0, 'Grass'] = 0

#best of encoding
if best_of == 3:
    pred_df.loc[0, 'best_of'] = 0
else:
    pred_df.loc[0, 'best_of'] = 1

pred_df.loc[0, 'minutes'] = match_time

#left/right hand encoding
if hand == 'Left':
    pred_df.loc[0, 'opp_hand'] = 1
else:
    pred_df.loc[0, 'opp_hand'] = 0

pred_df.loc[0, 'opp_ht'] = height
pred_df.loc[0, 'opp_age'] = age
pred_df.loc[0, 'opp_ace'] = aces
pred_df.loc[0, 'opp_df'] = double_faults
pred_df.loc[0, 'opp_svpt'] = serve_points
pred_df.loc[0,'opp_1stIn'] = first_in
pred_df.loc[0, 'opp_1stWon'] = first_won
pred_df.loc[0,'opp_2ndWon'] = second_won
pred_df.loc[0,'opp_bpSaved'] = breaks_save
pred_df.loc[0,'opp_bpFaced'] = breaks_faced

pred_df

#TO DO LIST:
#Turn DF into np array
#preprocess np array
#feed to prediction
#display prediction

#nice to have functionised code where possible (i.e. the if elses)
#also make look pretty

