import joblib
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from pydantic import BaseModel
import numpy as np


from pydantic import BaseModel

class StudentProfile(BaseModel):
  
    gender: str
    city_tier: str
    ssc_board: str
    hsc_board: str
    hsc_stream: str
    degree_field: str
    
    age: int
    ssc_percentage: float
    hsc_percentage: float
    degree_percentage: float
    mba_percentage: float
    internships_count: float
    projects_count: float
    certifications_count: float
    technical_skills_score: float
    soft_skills_score: float
    aptitude_score: float
    communication_score: float
    work_experience_months: float
    leadership_roles: float
    extracurricular_activities: float
    backlogs: float

  
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "gender": "Male",
                    "age": 22,
                    "city_tier": "Tier 1",
                    "ssc_percentage": 85.5,
                    "ssc_board": "CBSE",
                    "hsc_percentage": 82.0,
                    "hsc_board": "CBSE",
                    "hsc_stream": "Science",
                    "degree_percentage": 78.5,
                    "degree_field": "Computer Science",
                    "mba_percentage": 0.0,
                    "internships_count": 2,
                    "projects_count": 4,
                    "certifications_count": 3,
                    "technical_skills_score": 90.0,
                    "soft_skills_score": 85.0,
                    "aptitude_score": 88.0,
                    "communication_score": 80.0,
                    "work_experience_months": 6,
                    "leadership_roles": 1,
                    "extracurricular_activities": 2,
                    "backlogs": 0
                }
            ]
        }
    }

class PredictionResponse(BaseModel):
    placement: str
   


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("Loading model...")
        ml_models["placement_calculator"] = joblib.load("../campus_placement/models/best_model.pkl")
        print("Model loaded successfully.")
    except FileNotFoundError:
        print("Error: model.pkl not found.")
       
    
    yield 
  
    ml_models.clear()

app = FastAPI(lifespan=lifespan)


import pandas as pd 

@app.post("/predict", response_model=PredictionResponse)
async def predict_risk(student: StudentProfile):
    if "placement_calculator" not in ml_models:
        raise HTTPException(status_code=500, detail="Model not loaded")

    input_data = student.model_dump()

 
    df = pd.DataFrame([input_data])


    model = ml_models["placement_calculator"]
    
    try:
        prediction = model.predict(df)
        return {
            "placement": "Placed" if prediction[0] == 1 else "Not Placed"
        }
    except Exception as e:
     
        raise HTTPException(status_code=400, detail=str(e))