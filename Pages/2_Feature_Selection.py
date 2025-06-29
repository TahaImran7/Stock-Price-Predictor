import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


st.title("Feature Selection")

df = st.session_state.get("df")

if df is not None:
    features = st.multiselect("Select Features", options=df.columns.tolist())
    target = st.selectbox("Select Target Variable", options=df.columns.tolist())

    if features and target:
        try:
            st.session_state["features"] = features
            st.session_state["target"] = target

            st.subheader("Correlation Matrix")
            corr = df[features + [target]].corr()
            fig, ax = plt.subplots()
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error generating correlation matrix: {e}")
else:
    st.info("Please select both features and target variable to view the correlation matrix.")

col1, col2, col3 = st.columns([2, 7, 1])

with col1:
    if st.button("Previous"):
        st.switch_page("pages/1_Load_Data.py")

with col3:
    if st.button("Next"):
        st.switch_page("pages/3_Train_Test_Split.py")
