import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('./model.pkl','rb'))

gender = [0,1]

st.title('Number of Calories Burnt Predictor')
Gender = st.selectbox('Select your gender (0-male, 1-female)',sorted(gender))

col1, col2 = st.columns(2)
with col1:
    Age = st.number_input('Age')
with col2:
    Height = st.number_input('Height')

col3,col4,col5 = st.columns(3)

with col3:
    Duration = st.number_input('Exercise Duration (in mins)')
with col4:
    Heart_Rate = st.number_input('Heart Rate')
with col5:
    Body_Temp = st.number_input('Body Temp (in Celsius)')

if st.button('Predict Calories Burnt'):

    input_df =[Gender,Age,Height,Duration,Heart_Rate,Body_Temp]
    input_df = np.asarray(input_df)
    input_df = input_df.reshape(1,-1)
    result = model.predict(input_df)
    st.header("Calories burnt - " + str(int(result[0])))


