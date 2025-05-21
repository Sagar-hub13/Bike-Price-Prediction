
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Set up the page title
st.set_page_config(page_title="Bike Price Prediction", layout="centered")

st.title("🏍️ Bike Price Prediction App")
st.markdown("Enter the details of the bike below to estimate its market price.")

# Input form
brand = st.selectbox("Brand", ["Yamaha", "Honda", "Bajaj", "TVS", "Royal Enfield", "Hero", "Suzuki", "KTM"])
engine_cc = st.slider("Engine Capacity (CC)", 50, 500, 150)
mileage = st.slider("Mileage (km/l)", 20, 100, 50)
age = st.slider("Bike Age (Years)", 0, 15, 3)

# Encode brand
brand_dict = {
    "Yamaha": 0, "Honda": 1, "Bajaj": 2, "TVS": 3,
    "Royal Enfield": 4, "Hero": 5, "Suzuki": 6, "KTM": 7
}
brand_encoded = brand_dict[brand]

# Dummy prediction model (simulated logic)
def predict_price(brand, engine_cc, mileage, age):
    # Sample formula for demo
    base_price = 50000
    brand_factor = brand * 2000
    engine_factor = engine_cc * 100
    mileage_factor = mileage * 50
    depreciation = age * 3000
    price = base_price + brand_factor + engine_factor + mileage_factor - depreciation
    return round(price, 2)

# Predict button
if st.button("Predict Price"):
    price = predict_price(brand_encoded, engine_cc, mileage, age)
    st.success(f"Estimated Price of the Bike: ₹{price}")
