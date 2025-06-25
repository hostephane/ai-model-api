from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI()

# Charge le modèle à l'initialisation
model = joblib.load("model/model.pkl")

class InputData(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: InputData):
    prediction = model.predict([data.features])
    return {"prediction": prediction.tolist()}
