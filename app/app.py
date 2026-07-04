import streamlit as st
import joblib
import pandas as pd
loaded_model = joblib.load("house_price_model.pkl")