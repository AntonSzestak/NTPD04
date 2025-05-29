from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")

class InputData(BaseModel):
    features: list[float]

@app.get("/")
def root():
    return {"message": "API działa"}

@app.post("/predict")
def predict(data: InputData):
    if len(data.features) != 4:
        raise HTTPException(status_code=400, detail="Wymagane dokładnie 4 cechy wejściowe.")
    prediction = model.predict([data.features])[0]
    return {"prediction": int(prediction)}

@app.get("/info")
def info():
    return {"model": "LogisticRegression", "features": 4, "dataset": "iris"}

@app.get("/health")
def health():
    return {"status": "ok"}
