import streamlit as st
import pandas as pd
import joblib

model = joblib.load('fraud_detection_model.pkl')

st.title("Fraud Detection Prediction App")

st.markdown("Please enter the transaction details below: ")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrg = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=5000.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=6000.0)

if st.button("Predict"):
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrg],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })

    with st.spinner('Running fraud prediction...'):
        prediction = model.predict(input_data)

    st.markdown("---")
    st.markdown("#### Transaction Summary")
    st.table(input_data.T.rename(columns={0: 'Value'}))

    st.markdown("---")
    if prediction[0] == 1:
        st.error("🚨 This transaction is likely fraudulent.", icon="🚨")
        st.info("Please review the transaction details above.")
    else:
        st.success("✅ This transaction is likely legitimate.", icon="✅")
        st.info("No fraud detected for the provided transaction.")