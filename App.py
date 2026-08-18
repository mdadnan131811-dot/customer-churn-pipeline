import streamlit as st
import pandas as pd
import joblib

st.title("Customer Churn Prediction App")

tenure = st.number_input("Tenure (Months)", min_value=1, max_value=72, value=12)
monthly_charges = st.number_input("Monthly Charges ($)", min_value=20.0, max_value=120.0, value=50.0)
total_charges = st.number_input("Total Charges ($)", min_value=100.0, max_value=8000.0, value=600.0)
contract = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'])
payment_method = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer'])

if st.button("Predict Churn"):
    model = joblib.load('churn_model.pkl')
    input_data = pd.DataFrame({
        'Tenure': [tenure],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges],
        'Contract': [contract],
        'PaymentMethod': [payment_method]
    })
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("Warning: Customer is likely to churn!")
    else:
        st.success("Customer is likely to stay!")
  
