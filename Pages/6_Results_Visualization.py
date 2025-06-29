import streamlit as st
import matplotlib.pyplot as plt

st.title("Results Visualization")

model = st.session_state.get("model")
features = st.session_state.get("features")
predictions = st.session_state.get("predictions")
y_test = st.session_state.get("y_test_actual")
X_test = st.session_state.get("X_test")

if model is not None and predictions is not None and y_test is not None and X_test is not None:
    st.subheader("Feature Importance")
    if hasattr(model, "feature_importances_"):
        importance = model.feature_importances_
        fig, ax = plt.subplots()
        ax.barh(features, importance)
        ax.set_title("Feature Importance")
        st.pyplot(fig)
    else:
        st.info("This model does not support feature importance display.")

    st.subheader("Download Predictions")

    pred_df = X_test.copy()
    pred_df["Actual"] = y_test.values.flatten() if hasattr(y_test, "values") else y_test
    pred_df["Predicted"] = predictions

    csv = pred_df.to_csv(index=True)
    st.download_button("Download Predictions as CSV", csv, "predictions.csv", "text/csv")

else:
    st.warning("Prediction or model data missing. Train the model first.")

col1, col2, col3 = st.columns([2, 7, 1])
with col1:
    if st.button("Previous"):
        st.switch_page("pages/5_Evaluation_Metrics.py")

with col3:
    if st.button("Next"):
        st.switch_page("pages/7_Make_predictions.py")
