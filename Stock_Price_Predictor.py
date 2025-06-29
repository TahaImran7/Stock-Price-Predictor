import streamlit as st

st.set_page_config(page_title="Stock Price Predictor",layout="centered")

st.title("Welcome to Stock Price Predictor")

st.image("C:\\Users\\ISD\\Desktop\\TAHA\\CODES\\PROJECTS\\StockPricePredictor\\assets\\Welcome.jpg", use_container_width=True)

if st.button("Next",use_container_width=True):
    st.switch_page("pages/1_Load_Data.py")