import streamlit as st

st.title("Thank You For Using Stock Price Predictor")
st.text("Congrats Trader! You will now be rich😉")
st.image("C:\\Users\\ISD\\Desktop\\\CODES\\PROJECTS\\StockPricePredictor\\assets\\Thankyou.jpg", use_container_width=True)

st.text('Want to start over? Press the button below')
if st.button("Start Over",use_container_width=True):
    st.switch_page("pages/1_Load_Data.py")