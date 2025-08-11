import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load Model and Scaler
model = joblib.load('Youth_Resilience_Model.pkl')
scaler = joblib.load('scaler.pkl')

st.title('Youth Resilience Prediction Tool')
st.write('Predict which youths are most likely to benefit from Youth First Kenya interventions.')

# User Input
age = st.number_input('Age', min_value=10, max_value=35, value=20)
gender = st.selectbox('Gender', ['Male', 'Female'])
education = st.selectbox('Education Level', ['Primary', 'Secondary', 'Tertiary'])
employment = st.selectbox('Employment Status', ['Employment', 'Unemployment', 'Student'])
mental_score = st.slider('Baseline Mental Health Score', 0, 100, 50)
resilience_score = st.slider('Resilience Score at Intake', 0, 100, 50)
social_support = st.slider('Social Support Rating', 0, 10, 5)

# Converting categorical to numeric
data = pd.DataFrame({
    "Age": [age],
    "BaselineMentalHealthScore": [mental_score],
    "ResilienceScore": [resilience_score],
    "SocialSupportRating": [social_support],
    "Gender_Male": [1 if gender == "Male" else 0],
    "EducationLevel_Secondary": [1 if education == "Secondary" else 0],
    "EducationLevel_Tertiary": [1 if education == "Tertiary" else 0],
    "EmploymentStatus_Student": [1 if employment == "Student" else 0],
    "EmploymentStatus_Unemployed": [1 if employment == "Unemployed" else 0]
})

# Scale numeric features
data_scaled = scaler.transform(data)

# Function to generate personalized recommendations
def generate_recommendations(mental, resilience, support, employment):
    recs = []
    
    # Mental health
    if mental < 50:
        recs.append("Enroll in mental health counseling or stress management programs.")
    else:
        recs.append("Maintain healthy coping strategies and continue mental wellness check-ins.")
    
    # Resilience
    if resilience < 50:
        recs.append("Participate in resilience training workshops to build adaptive skills.")
    else:
        recs.append("Engage in leadership or mentorship activities to strengthen resilience further.")
    
    # Social support
    if support < 5:
        recs.append("Join peer-support groups or community activities to expand your support network.")
    else:
        recs.append("Keep nurturing existing social connections to maintain strong support.")
    
    # Employment
    if employment == "Unemployment":
        recs.append("Explore vocational training or job placement programs to improve economic stability.")
    elif employment == "Student":
        recs.append("Access academic mentorship and career guidance resources.")
    else:
        recs.append("Seek opportunities for career growth and skills advancement.")
    
    return recs

# Prediction
if st.button('Predict'):
    prob = model.predict_proba(data_scaled)[0][1]
    if prob > 0.5:
        st.success(f'High Benefit Likelihood ({prob:.2%}) ✅')
    else:
        st.warning(f'Low Benefit Likelihood ({prob:.2%}) ⚠️')
    
    # Show personalized recommendations
    st.subheader("Personalized Recommendations")
    recommendations = generate_recommendations(mental_score, resilience_score, social_support, employment)
    for rec in recommendations:
        st.write(f"- {rec}")