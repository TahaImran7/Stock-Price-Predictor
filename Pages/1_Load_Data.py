import streamlit as st
import pandas as pd

st.title("Load Your Stock Data (Apple Stock)")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state["df"] = df
    st.dataframe(df.head())


col1, col2, col3 = st.columns([2, 7, 1])
with col1:
    if st.button("Previous"):
        st.switch_page("Stock_Price_Predictor.py")

with col3:
    if st.button("Next"):
        st.switch_page("pages/2_Feature_Selection.py")
