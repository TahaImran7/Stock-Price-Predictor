# 📈 Stock Price Predictor Web App

An interactive machine learning web application built using **Streamlit** and **Python** for forecasting stock prices. It combines powerful ML models (Random Forest & XGBoost) with intuitive visualizations to deliver meaningful financial insights.

⚠️ **Disclaimer**: This project is intended for educational and informational purposes only. Stock price predictions are inherently uncertain and trading carries significant financial risk.
I am not a financial advisor — always do your own research (DYOR) and consult with a qualified professional before making any investment decisions. Use this tool at your own discretion Thank You.

---

## AUTHOR Information

- **Taha Imran**
- **Email**: tahaimran315@gmail.com -- [Email Me](mailto:tahaimran315@gmail.com)
- **LinkedIn**: www.linkedin.com/in/taha-imran-9a6987338 -- [Taha Imran](www.linkedin.com/in/taha-imran-9a6987338)

---

## Technologies Used

- **Python**  
- **Streamlit** (for Web Interface)  
- **Scikit-learn**, **XGBoost** (for ML Models)  
- **Pandas**, **NumPy** (for Data Processing)  
- **Matplotlib**, **Plotly** (for Data Visualization)

---

## Features

- **Historical Data Preprocessing**: Clean and structure raw stock data for modeling.
- **Machine Learning Models**: Forecast stock prices using:
  - Random Forest Regressor
  - XGBoost Regressor
- **Interactive Visualizations**:
  - Time-series plotting of real vs predicted prices
  - Model performance comparisons
- **Dynamic Inputs**:
  - Select different price input (Open, High, Low, Close)

---

## Machine Learning Workflow

1. **Data Loading**: Import historical stock prices from CSV.
2. **Feature Selection**: Selecting required features from the dataset.
3. **Train Test Split**: Splitting training and testing set for time series split.
4. **Model Training**: Fit and train Random Forest and XGBoost models on training data.
5. **Prediction & Evaluation**: Predict future prices and compare model metrics.
6. **Visualization**: Plot results for easy interpretation.
6. **Making live predictions**: Input current price (Open, High, Low, Close) to make predictions for the next day price for High candle.

---

## How to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/TahaImran7/Stock-Price-Predictor.git

2. **Navigate to Project Folder**
   ```bash
   cd StockPricePredictor

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run the Streamlit Webapp through the terminal**
   ```bash
   streamlit run Stock_Price_Predictor.py

5. **Navigate to**
   ```bash
   http://localhost:8501

# 🤝 **Contributing**
Feel free to fork the repo, suggest improvements, or raise issues. All contributions are welcome!
