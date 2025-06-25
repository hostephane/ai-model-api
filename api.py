from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Charger le modèle
MODEL_PATH = "models/random_forest_model_2/model.pkl"
model = joblib.load(MODEL_PATH)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({"prediction": prediction.tolist()})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
