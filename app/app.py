import streamlit as st
import joblib
import pandas as pd
loaded_model = joblib.load("../models/house_price_model.pkl")
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Enter the property details below to estimate the house price.")

locations = [
    "thane", "navi-mumbai", "nagpur", "mumbai", "ahmedabad",
    "bangalore", "chennai", "gurgaon", "hyderabad", "indore",
    "jaipur", "kolkata", "lucknow", "new-delhi", "noida",
    "pune", "agra", "ahmadnagar", "allahabad", "aurangabad",
    "badlapur", "belgaum", "bhiwadi", "bhiwandi", "bhopal",
    "bhubaneswar", "chandigarh", "coimbatore", "dehradun",
    "durgapur", "ernakulam", "faridabad", "ghaziabad", "goa",
    "greater-noida", "guntur", "guwahati", "gwalior",
    "haridwar", "jabalpur", "jamshedpur", "jodhpur", "kalyan",
    "kanpur", "kochi", "kozhikode", "ludhiana", "madurai",
    "mangalore", "mohali", "mysore", "nashik", "navsari",
    "nellore", "palakkad", "palghar", "panchkula", "patna",
    "pondicherry", "raipur", "rajahmundry", "ranchi",
    "satara", "shimla", "siliguri", "solapur", "sonipat",
    "surat", "thrissur", "tirupati", "trichy", "trivandrum",
    "udaipur", "udupi", "vadodara", "vapi", "varanasi",
    "vijayawada", "visakhapatnam", "vrindavan", "zirakpur"
]

col1, col2 = st.columns(2)

with col1:
    location = st.selectbox("Location", sorted(locations))

    transaction = st.selectbox(
        "Transaction",
        ["Resale", "New Property", "Other", "Rent/Lease"]
    )

    furnishing = st.selectbox(
        "Furnishing",
        ["Unfurnished", "Semi-Furnished", "Furnished"]
    )

    facing = st.selectbox(
        "Facing",
        [
            "East",
            "North",
            "South",
            "West",
            "North - East",
            "North - West",
            "South - East",
            "South -West"
        ]
    )

    overlooking = st.selectbox(
        "Overlooking",
        [
            "Garden/park",
            "Main road",
            "Pool",
            "Garden/park, main road",
            "Garden/park, pool",
            "Garden/park, pool, main road",
            "Garden/park, main road, pool",
            "Pool, garden/park",
            "Pool, garden/park, main road",
            "Pool, main road",
            "Pool, main road, garden/park",
            "Main road, garden/park",
            "Main road, garden/park, pool",
            "Main road, pool",
            "Main road, pool, garden/park",
            "Garden/park, not available",
            "Main road, not available"
        ]
    )

with col2:

    ownership = st.selectbox(
        "Ownership",
        [
            "Freehold",
            "Leasehold",
            "Co-operative Society",
            "Power Of Attorney"
        ]
    )

    bhk = st.number_input("BHK", min_value=1, max_value=20, value=2)

    bathroom = st.number_input("Bathrooms", min_value=1, max_value=20, value=2)

    balcony = st.number_input("Balconies", min_value=0, max_value=10, value=1)

    carpet_area = st.number_input(
        "Carpet Area (sq.ft.)",
        min_value=100.0,
        value=1000.0
    )

    current_floor = st.number_input(
        "Current Floor",
        min_value=0,
        max_value=100,
        value=1
    )

    total_floor = st.number_input(
        "Total Floors",
        min_value=1,
        max_value=100,
        value=10
    )

floor_ratio = current_floor / total_floor

if st.button("Predict House Price"):

    input_df = pd.DataFrame({
        "location": [location],
        "Transaction": [transaction],
        "Furnishing": [furnishing],
        "facing": [facing],
        "overlooking": [overlooking],
        "Bathroom": [bathroom],
        "Balcony": [balcony],
        "Ownership": [ownership],
        "Bhk": [bhk],
        "Carpet_area_sqft": [carpet_area],
        "Current_floor": [current_floor],
        "Total_floor": [total_floor],
        "floor_ratio": [floor_ratio]
    })

    prediction = loaded_model.predict(input_df)

    st.success(f"🏠 Estimated House Price: ₹ {prediction[0]:,.0f}")
    
