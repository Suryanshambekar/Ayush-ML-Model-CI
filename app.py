<<<<<<< HEAD
import streamlit as st
import numpy as np
import joblib

# Load the trained model and scaler
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

# Streamlit app title and description
st.title("Loan Approval Prediction App")
st.write("""
This app predicts whether a loan will be approved based on user input. 
Fill in the form below to get a prediction.
""")

# Create input fields for each feature
person_age = st.number_input("Person's Age", min_value=18, max_value=100, step=1)
person_gender = st.selectbox("Person's Gender", ["Male", "Female"])
person_education = st.selectbox("Education Level", ["High School", "Undergraduate", "Postgraduate"])
person_income = st.number_input("Annual Income (in USD)", min_value=10000, max_value=1000000, step=1000)
person_emp_exp = st.number_input("Years of Employment Experience", min_value=0, max_value=50, step=1)
person_home_ownership = st.selectbox("Home Ownership", ["Rent", "Own", "Mortgage"])
loan_amnt = st.number_input("Loan Amount (in USD)", min_value=1000, max_value=100000, step=500)
loan_intent = st.selectbox("Loan Intent", ["Home Improvement", "Debt Consolidation", "Education", "Medical", "Vacation", "Other"])
loan_int_rate = st.number_input("Loan Interest Rate (%)", min_value=0.0, max_value=50.0, step=0.1)
loan_percent_income = st.slider("Loan Percent of Income (%)", min_value=0.0, max_value=1.0, step=0.01)
cb_person_cred_hist_length = st.number_input("Credit History Length (in years)", min_value=0, max_value=50, step=1)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, step=1)
previous_loan_defaults_on_file = st.selectbox("Previous Loan Defaults?", ["No", "Yes"])

# Encoding categorical inputs
gender_map = {"Male": 0, "Female": 1}
education_map = {"High School": 0, "Undergraduate": 1, "Postgraduate": 2}
home_ownership_map = {"Rent": 0, "Own": 1, "Mortgage": 2}
loan_intent_map = {
    "Home Improvement": 0, "Debt Consolidation": 1, "Education": 2,
    "Medical": 3, "Vacation": 4, "Other": 5
}
previous_loan_defaults_map = {"No": 0, "Yes": 1}

# Create feature vector for prediction
input_data = np.array([
    person_age,
    gender_map[person_gender],
    education_map[person_education],
    person_income,
    person_emp_exp,
    home_ownership_map[person_home_ownership],
    loan_amnt,
    loan_intent_map[loan_intent],
    loan_int_rate,
    loan_percent_income,
    cb_person_cred_hist_length,
    credit_score,
    previous_loan_defaults_map[previous_loan_defaults_on_file]
]).reshape(1, -1)

# Button to make predictions
if st.button("Predict Loan Status"):
    # Scale the input data
    input_data_scaled = scaler.transform(input_data)
    # Make prediction
    prediction = model.predict(input_data_scaled)
    # Output result
    loan_status = "Approved" if prediction[0] == 1 else "Rejected"
    st.success(f"The loan is likely to be: {loan_status}")
=======
import streamlit as st
import numpy as np
import joblib

# Load the trained model and scaler
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

# Streamlit app title and description
st.title("Loan Approval Prediction App")
st.write("""
This app predicts whether a loan will be approved based on user input. 
Fill in the form below to get a prediction.
""")

# Create input fields for each feature
person_age = st.number_input("Person's Age", min_value=18, max_value=100, step=1)
person_gender = st.selectbox("Person's Gender", ["Male", "Female"])
person_education = st.selectbox("Education Level", ["High School", "Undergraduate", "Postgraduate"])
person_income = st.number_input("Annual Income (in USD)", min_value=10000, max_value=1000000, step=1000)
person_emp_exp = st.number_input("Years of Employment Experience", min_value=0, max_value=50, step=1)
person_home_ownership = st.selectbox("Home Ownership", ["Rent", "Own", "Mortgage"])
loan_amnt = st.number_input("Loan Amount (in USD)", min_value=1000, max_value=100000, step=500)
loan_intent = st.selectbox("Loan Intent", ["Home Improvement", "Debt Consolidation", "Education", "Medical", "Vacation", "Other"])
loan_int_rate = st.number_input("Loan Interest Rate (%)", min_value=0.0, max_value=50.0, step=0.1)
loan_percent_income = st.slider("Loan Percent of Income (%)", min_value=0.0, max_value=1.0, step=0.01)
cb_person_cred_hist_length = st.number_input("Credit History Length (in years)", min_value=0, max_value=50, step=1)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, step=1)
previous_loan_defaults_on_file = st.selectbox("Previous Loan Defaults?", ["No", "Yes"])

# Encoding categorical inputs
gender_map = {"Male": 0, "Female": 1}
education_map = {"High School": 0, "Undergraduate": 1, "Postgraduate": 2}
home_ownership_map = {"Rent": 0, "Own": 1, "Mortgage": 2}
loan_intent_map = {
    "Home Improvement": 0, "Debt Consolidation": 1, "Education": 2,
    "Medical": 3, "Vacation": 4, "Other": 5
}
previous_loan_defaults_map = {"No": 0, "Yes": 1}

# Create feature vector for prediction
input_data = np.array([
    person_age,
    gender_map[person_gender],
    education_map[person_education],
    person_income,
    person_emp_exp,
    home_ownership_map[person_home_ownership],
    loan_amnt,
    loan_intent_map[loan_intent],
    loan_int_rate,
    loan_percent_income,
    cb_person_cred_hist_length,
    credit_score,
    previous_loan_defaults_map[previous_loan_defaults_on_file]
]).reshape(1, -1)

# Button to make predictions
if st.button("Predict Loan Status"):
    # Scale the input data
    input_data_scaled = scaler.transform(input_data)
    # Make prediction
    prediction = model.predict(input_data_scaled)
    # Output result
    loan_status = "Approved" if prediction[0] == 1 else "Rejected"
    st.success(f"The loan is likely to be: {loan_status}")
>>>>>>> 11dd4da56aab254c59cb418873974c8a93e84c7a
