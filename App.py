import joblib
import streamlit as st
import pandas as pd
# import scikit-learn
# import numpy

#Load the model binary file

model = joblib.load('linear_regression_model.pkl')

#creating App

st.title('Aircraft Fuel Condsumption Predictor')

flight_distance = st.number_input('Flight Distance(km)')
number_of_passenger = st.number_input('Number Of Passenger')
flight_duration = st.number_input('Flight Duration')
aircraft_type = st.selectbox('Aircraft Type',['Type1','Type2','Type3'])

input_data = pd.DataFrame(
    {
        'Flight_Distance': [flight_distance],
        'Number_of_Passengers':[number_of_passenger],
        'Flight_Duration':[flight_duration],
        'Aircraft_Type_Type1':[1 if aircraft_type == 'Type1' else 0],
        'Aircraft_Type_Type2':[1 if aircraft_type == 'Type2' else 0],
        'Aircraft_Type_Type3':[1 if aircraft_type == 'Type3' else 0]
        
    }
)

if st.button('Predict'):
    Fuel_Consumption = model.predict(input_data)
    st.write(Fuel_Consumption)