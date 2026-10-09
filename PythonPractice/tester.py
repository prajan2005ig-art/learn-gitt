import streamlit as st
import pandas as pd
import joblib


@st.cache_resource
def load_model():
    return joblib.load("admission_model.pkl")


model = load_model()

st.title("University Admission Predictor")

st.write("Enter your academic details below.")

cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

ielts_overall = st.number_input(
    "IELTS Overall",
    min_value=0.0,
    max_value=9.0,
    value=6.5,
    step=0.5
)

projects = st.number_input(
    "Number of Projects",
    min_value=0,
    step=1
)

internship = st.selectbox(
    "Internship Experience",
    ["No", "Yes"]
)

research = st.selectbox(
    "Research Experience",
    ["No", "Yes"]
)

if st.button("Predict"):

    input_data = pd.DataFrame([{
        "cgpa": cgpa,
        "ielts_overall": ielts_overall,
        "projects": projects,
        "internship": internship,
        "research": research
    }])

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")
    st.write(f"Predicted outcome: **{prediction}**")

    st.caption(
        "Educational demonstration using a model trained on synthetic data. "
        "This result is not a real university admission decision."
    )