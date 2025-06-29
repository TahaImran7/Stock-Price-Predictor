import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

st.title("Evaluation Metrics")

predictions = st.session_state.get("predictions")
y_test = st.session_state.get("y_test_actual")
X_test = st.session_state.get("X_test")

if predictions is not None and y_test is not None:
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)

    st.subheader("Metrics:")
    st.write(f"**Mean Absolute Error (MAE):** {mae:.2f}")
    st.write(f"**Mean Squared Error (MSE):** {mse:.2f}")
    st.write(f"**Root Mean Squared Error (RMSE):** {rmse:.2f}")
    st.write(f"**R² Score:** {r2:.2f}")

    st.subheader("Actual vs Predicted")
    fig, ax = plt.subplots()
    ax.plot(y_test.index, y_test, label="Actual", color='blue')
    ax.plot(y_test.index, predictions, label="Predicted", color='orange')
    ax.legend()
    st.pyplot(fig)

else:
    st.warning("Model not trained or data missing.")

col1, col2, col3 = st.columns([2, 7, 1])
with col1:
    if st.button("Previous"):
        st.switch_page("pages/4_Model_Training.py")

with col3:
    if st.button("Next"):
        st.switch_page("pages/6_Results_Visualization.py")
