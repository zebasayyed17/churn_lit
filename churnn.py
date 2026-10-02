import streamlit as st
import pandas as pd
import pickle


# -----------------------------
# Load trained model
# -----------------------------
with open("churn_model.pkl", "rb") as file:
    model = pickle.load(file)


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------
st.title("📊 Customer Churn Prediction")
st.write("Enter the customer details below to predict whether the customer is likely to churn.")


# -----------------------------
# Input fields
# -----------------------------
st.subheader("Customer Information")

col1, col2, col3 = st.columns(3)

with col1:
    call_failure = st.number_input(
        "Call Failure",
        min_value=0,
        value=0
    )

    complains = st.number_input(
        "Complains",
        min_value=0,
        value=0
    )

    subscription_length = st.number_input(
        "Subscription Length",
        min_value=0,
        value=12
    )

    charge_amount = st.number_input(
        "Charge Amount",
        min_value=0,
        value=0
    )


with col2:
    seconds_of_use = st.number_input(
        "Seconds of Use",
        min_value=0,
        value=1000
    )

    frequency_of_use = st.number_input(
        "Frequency of Use",
        min_value=0,
        value=10
    )

    frequency_of_sms = st.number_input(
        "Frequency of SMS",
        min_value=0,
        value=10
    )

    distinct_called_numbers = st.number_input(
        "Distinct Called Numbers",
        min_value=0,
        value=5
    )


with col3:
    age_group = st.number_input(
        "Age Group",
        min_value=0,
        value=3
    )

    tariff_plan = st.number_input(
        "Tariff Plan",
        min_value=0,
        value=1
    )

    status = st.number_input(
        "Status",
        min_value=0,
        value=1
    )

    customer_value = st.number_input(
        "Customer Value",
        min_value=0.0,
        value=100.0
    )


# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Predict Churn", use_container_width=True):

    input_data = pd.DataFrame({
        'Call  Failure': [call_failure],
        'Complains': [complains],
        'Subscription  Length': [subscription_length],
        'Charge  Amount': [charge_amount],
        'Seconds of Use': [seconds_of_use],
        'Frequency of use': [frequency_of_use],
        'Frequency of SMS': [frequency_of_sms],
        'Distinct Called Numbers': [distinct_called_numbers],
        'Age Group': [age_group],
        'Tariff Plan': [tariff_plan],
        'Status': [status],
        'Customer Value': [customer_value]
    })

    # Prediction
    prediction = model.predict(input_data)[0]

    # Probability
    probability = model.predict_proba(input_data)[0]

    churn_probability = probability[1] * 100
    no_churn_probability = probability[0] * 100


    # -----------------------------
    # Display result
    # -----------------------------
    st.subheader("Prediction Result")

    if prediction == 1:

        st.error("⚠️ Customer is likely to CHURN")

        st.write(
            f"**Churn Probability:** {churn_probability:.2f}%"
        )

    else:

        st.success("✅ Customer is likely to STAY")

        st.write(
            f"**Churn Probability:** {churn_probability:.2f}%"
        )


    # Probability chart
    result = pd.DataFrame({
        "Prediction": ["Stay", "Churn"],
        "Probability": [
            no_churn_probability,
            churn_probability
        ]
    })

    st.bar_chart(
        result.set_index("Prediction")
    )