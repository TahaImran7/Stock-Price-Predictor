import streamlit as st
import pickle
# from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor as xgbr

st.title("Model Training")

rfr_model = pickle.load(open('C:\\Users\\ISD\\Desktop\\TAHA\\CODES\\PROJECTS\\StockPricePredictor\\Models(Colab & PDF File)\\rfr_stock_predictor.pkl', 'rb'))
# xgbr_model = pickle.load(open('C:\\Users\\ISD\\Desktop\\TAHA\\CODES\\PROJECTS\\StockPricePredictor\\Models(Colab & PDF File)\\xgbr_stock_predictor.pkl', 'rb'))
xgbr_model = xgbr(learning_rate = 0.1,max_depth = 1, n_estimators = 150)
models = {
    "Random Forest Regressor": rfr_model,
    "XGBoost Regressor": xgbr_model
}

# models = {
#     "Random Forest Regressor": RandomForestRegressor(n_estimators=100,max_depth=6,random_state=42),
#     "XGBoost Regressor": XGBRegressor(learning_rate=0.1, max_depth=1, n_estimators=150)
# }

X_train = st.session_state.get("X_train")
y_train = st.session_state.get("y_train")
X_test = st.session_state.get("X_test")
y_test = st.session_state.get("y_test")
features = st.session_state.get("features")
target = st.session_state.get("target")

if X_train is not None and y_train is not None and features and target:
    model_choice = st.selectbox("Select Model", list(models.keys()))

    if st.button("Train Model"):
        model = models[model_choice]

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        st.session_state["model"] = model
        st.session_state["predictions"] = predictions
        st.session_state["y_test_actual"] = y_test

        st.success("Model Trained Successfully!")

else:
    st.warning("Ensure you've performed train-test split and selected features/target.")

col1, col2, col3 = st.columns([2, 7, 1])
with col1:
    if st.button("Previous"):
        st.switch_page("pages/3_Train_Test_Split.py")

with col3:
    if st.button("Next"):
        st.switch_page("pages/5_Evaluation_Metrics.py")
