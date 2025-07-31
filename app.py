import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("best_salary_model.pkl")

st.title("💼 Salary Prediction App")

education = st.selectbox("Education Level", [0, 1, 2], format_func=lambda x: ["High School", "Bachelor's", "Master's/PhD"][x])
experience = st.number_input("Years of Experience", 0, 40, step=1)
location = st.selectbox("Location", [0, 1, 2], format_func=lambda x: ["City A", "City B", "City C"][x])
job_title = st.selectbox("Job Title", [0, 1, 2], format_func=lambda x: ["Developer", "Manager", "Analyst"][x])
age = st.number_input("Age", 18, 70, step=1)
gender = st.selectbox("Gender", [0, 1], format_func=lambda x: ["Male", "Female"][x])

if st.button("Predict Salary"):
    data = pd.DataFrame([[education, experience, location, job_title, age, gender]],
                        columns=["Education", "Experience", "Location", "Job_Title", "Age", "Gender"])
    salary = model.predict(data)[0]
    st.success(f"Predicted Salary: ₹{salary:,.2f}")
