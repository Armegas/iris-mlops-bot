import streamlit as st
import requests
from mlflow.tracking import MlflowClient

st.title("📊 Comparación de Modelos - Iris")

client = MlflowClient()
runs = client.search_runs(experiment_ids=["0"], order_by=["metrics.accuracy DESC"])

for run in runs:
    st.subheader(run.data.params["model"])
    st.write(f"Accuracy: {run.data.metrics['accuracy']:.2f}")

st.markdown("---")
st.header("🔍 Predicción en tiempo real")

sepal_length = st.number_input("Sepal Length", value=5.1)
sepal_width = st.number_input("Sepal Width", value=3.5)
petal_length = st.number_input("Petal Length", value=1.4)
petal_width = st.number_input("Petal Width", value=0.2)

if st.button("Predecir Clase"):
    params = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    response = requests.get("http://fastapi:8000/predict", params=params)
    if response.status_code == 200:
        st.success(f"Clase predicha: {response.json()['class']}")
    else:
        st.error("Error en la predicción")