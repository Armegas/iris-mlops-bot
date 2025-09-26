# fastapi_service/main.py

from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()
model = pickle.load(open("models/trained_model.pkl", "rb"))

@app.get("/predict")
def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(data)
    return {"class": int(prediction[0])}
