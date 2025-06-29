import streamlit as st
import numpy as np

st.title("Live Predictions")

model = st.session_state.get("model")
features = st.session_state.get("features")

if model is not None and features:
    st.subheader("Enter Input Values")

    inputs = {}
    for feature in features:
        inputs[feature] = st.number_input(f"{feature} Price", format="%.5f")

    if st.button("Predict"):
        input_data = np.array([list(inputs.values())]).reshape(1, -1)
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted High Price (Next Day): {prediction:.5f}")
else:
    st.warning("Model not trained or feature selection missing.")


col1, col2, col3 = st.columns([2, 7, 1])
with col1:
    if st.button("Previous"):
        st.switch_page("pages/6_Results_Visualization.py")

with col3:
    if st.button("Next"):
        st.switch_page("pages/8_Thank_You.py")