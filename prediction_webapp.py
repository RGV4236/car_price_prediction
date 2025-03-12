# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 00:38:59 2025

@author: gowri
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('C:/Users/gowri/OneDrive/Desktop/model/trained_model_lass.sav', 'rb'))
loaded_model = pickle.load(open('trained_model_lass.sav', 'rb'))


#creating a function for prediction

def predict_car_price(year, present_price, kms_driven, fuel_type, seller_type, transmission, owner):
    # Load the trained model

    # Encode categorical features
    fuel_type_encoded = 0 if fuel_type == "Petrol" else 1 if fuel_type == "Diesel" else 2
    seller_type_encoded = 0 if seller_type == "Dealer" else 1
    transmission_encoded = 0 if transmission == "Manual" else 1
    age=year
    # Create input array for prediction
    features = np.array([[age, present_price, kms_driven, fuel_type_encoded, seller_type_encoded, transmission_encoded, owner]])
    predicted_price = loaded_model.predict(features)
    st.success(f"💰 Predicted Selling Price: ₹{predicted_price.item():.2f} lakhs")



def main():
    
    
    #giving a title
    st.title('Vehicle Price Prediction Web App')
    
    #getting the input data from the user
    
    st.write("Enter the car details below to get a price prediction.")

    # Input fields for user data
    year = st.number_input("Car Year", min_value=1999, max_value=2025, step=1)
    present_price = st.number_input("Present Price (in lakhs)", min_value=0.0, step=0.1)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, step=100)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])
    owner = st.number_input("Number of Previous Owners", min_value=0, step=1)
    # Calculate the car's age
    current_year = 2025  
    age = current_year - year

    pred = ''
  
    #creating a button
    if st.button("Predicted Price"):
        # Create input array for prediction
        pred = predict_car_price(age, present_price, kms_driven, fuel_type, seller_type, transmission, owner)
        # Predict using the model
        
    st.success(pred)
    

if __name__ == '__main__':
    main()
    

    
