import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Train Test Split")
st.text("Train Data: 04-Jan-2021 - 31-Dec-2024")
st.text("Test Data: 01-Jan-2025 - 02-Jun-2025")

df = st.session_state.get("df")
if df is not None:
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.set_index('Date')
        st.session_state["df"] = df

    df = df['2021-04-01':]

    split_date = '2025-01-05'
    train = df[df.index < split_date]
    test = df[df.index >= split_date]

    st.session_state["train_data"] = train
    st.session_state["test_data"] = test

    st.session_state["X_train"] = train[st.session_state["features"]]
    st.session_state["y_train"] = train[st.session_state["target"]]
    st.session_state["X_test"] = test[st.session_state["features"]]
    st.session_state["y_test"] = test[st.session_state["target"]]

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(train.index, train[st.session_state["target"]], label="Train")
    ax.plot(test.index, test[st.session_state["target"]], label="Test")

    ax.set_title("Train/Test Split on Time Series")
    ax.set_xlabel("Date")
    ax.set_ylabel(st.session_state["target"])
    ax.legend()
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

    st.session_state["train_data"] = train
    st.session_state["test_data"] = test

else:
    st.warning("Data not loaded. Please upload it in the Load Data page.")

col1, col2, col3 = st.columns([2, 7, 1])
with col1:
    if st.button("Previous"):
        st.switch_page("pages/2_Feature_Selection.py")

with col3:
    if st.button("Next"):
        st.switch_page("pages/4_Model_Training.py")
