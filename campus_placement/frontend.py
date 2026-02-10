import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Student Placement Predicator")
st.markdown("Enter the necessary data to predict if you would get a placement")

with st.form("sentiment_form"):
    age = st.number_input("Enter your age", min_value=10, max_value=30, format="%d")
    gender = st.selectbox(
    "Enter your gender",
    ("Male", "Female"),
    )
    city_tier = st.selectbox(
    "Enter your city tier",
    ("Tier 1", "Tier 2", "Tier 3"),
    )
    
    ssc_board = st.selectbox(
    "Enter your SSC board",
    ("CBSE", "State", "ICSE"),
    )
     
    hsc_board = st.selectbox(
    "Enter your HSC board",
    ("CBSE", "State", "ICSE"),
    )
    
    hsc_stream = st.selectbox(
    "Enter your HSC stream",
    ("Science", "Commerce","Arts"),
    )
    degree_field = st.selectbox(
    "Enter your degree field",
    ("Engineering", "Business", "Arts", "Other"),
    )
    
    
    ssc_percentage = st.number_input("Enter SSC percentage", min_value=0.0, max_value=100.0, format="%1f")
    hsc_percentage = st.number_input("Enter HSC percentage", min_value=0.0, max_value=100.0, format="%1f")
    degree_percentage = st.number_input("Enter degree percentage", min_value=0.0, max_value=100.0, format="%1f")
    mba_percentage = st.number_input("Enter MBA percentage", min_value=0.0, max_value=100.0, format="%1f")
    internship_count = st.number_input("Enter internship count", min_value=0, max_value=5, format="%d")
    project_count = st.number_input("Enter project count", min_value=0, max_value=10, format="%d")
    certification_count = st.number_input("Enter certification count", min_value=0, max_value=10, format="%d")
    technical_skills_score = st.number_input("Enter technical skills score", min_value=0, max_value=10, format="%d")
    soft_skills_score = st.number_input("Enter soft skills score", min_value=0, max_value=10, format="%d")
    aptitude_score = st.number_input("Enter aptitude score", min_value=0.0, max_value=100.0, format="%1f")
    work_expericence = st.number_input("Enter work experience months", min_value=0, max_value=36, format="%d")
    leadership_roles = st.number_input("Enter number of leadership roles you have",min_value=0, max_value=10, format="%d")
    extracurrilar_activities = st.number_input("Enter number of extracurricular activities you have partaken in", min_value=0, max_value=10, format="%d")
    communication_score = st.number_input("Enter your communication score", min_value=0, max_value=10, format="%d")
    backlogs = st.number_input("Enter backlogs",  min_value=0, max_value=10, format="%d")
    
    submitted = st.form_submit_button("Predict")


if submitted:
    try:
      
        payload = {
  "age": age,
  "gender": gender,
  "city_tier": city_tier,
  "ssc_board": ssc_board,
  "hsc_board": hsc_board,
  "hsc_stream": hsc_stream,
  "degree_field": degree_field,
  "ssc_percentage": ssc_percentage,
  "hsc_percentage": hsc_percentage,
  "degree_percentage": degree_percentage,
  "mba_percentage": mba_percentage,
  "internships_count": internship_count,
  "projects_count": project_count,
  "certifications_count": certification_count,
  "technical_skills_score": technical_skills_score,
  "soft_skills_score": soft_skills_score,
  "aptitude_score": aptitude_score,
  "work_experience_months": work_expericence,
  "leadership_roles": leadership_roles,
  "extracurricular_activities": extracurrilar_activities,
  "communication_score" :communication_score,
  "backlogs": backlogs
}
        response = requests.post(API_URL, json=payload)
        
   
        if response.status_code == 200:
            data = response.json()
            
          
            if data['placement'] == "Placed":
                st.success(f"You have a high chance of getting placed")
            else:
                st.error("You are not likely to get a placement")
                    
        else:
            st.error(f"Backend Error: {response.status_code}")
            st.json(response.json())
            
    except requests.exceptions.ConnectionError:
        st.error("Connection Refused: Internal Server Error")