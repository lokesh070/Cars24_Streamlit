import streamlit as st
import pickle
import numpy as np
import pandas as pd


st.header('Car Price Prediction App')

#df = pd.read_csv('car_prices.csv')
#st.dataframe(df)
col1, col2 = st.columns(2)
with col1:
    year = st.number_input("Enter the Year of Vehicle")

with col2:
    fuel_type_input = st.selectbox(
        "Choose the Fuel Type",
        ("Diesel", "Petrol", "CNG", "LPG", "Electric"), )

col1, col2 = st.columns(2)
with col1:
    transmission_type_input = st.selectbox(
        "Choose the Transmission Type",
        ("Manual", "Automatic"), )

with col2:
    seats = st.selectbox( "Choose the seat Type", [4, 5, 6, 7, 8, 9, 11], )

engine = st.slider("Engine CC", 800, 5000, 700)



encode_dict = {
    "fuel_type": {'Diesel':1, 'Petrol': 2, 'CNG':3, 'LPG':4, 'Electric':5},
    "seller_type": {'Dealer':1, 'Individual': 2, 'Trustmark Dealer':3},
    "transmission_type": {'Manual':1, 'Automatic': 2}
}

encoded_fuel = encode_dict['fuel_type'][fuel_type_input]
encoded_transmission = encode_dict['transmission_type'][transmission_type_input]

def model_pred(year, encoded_fuel, encoded_transmission, engine, seats ):
    with open('car_pred','rb') as file:
        model = pickle.load(file)
        input_features = [[year, 2, 120000, encoded_fuel, encoded_transmission,19.7, engine, 46.3, seats]]
        return model.predict(input_features)

if st.button("Predict"):
    predicted_prcie = model_pred(year, encoded_fuel, encoded_transmission, engine, seats)
    st.write(str(predicted_prcie), " Lakhs")