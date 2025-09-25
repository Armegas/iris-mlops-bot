import streamlit as st
from mlflow.tracking import MlflowClient

st.title("📊 Comparación de Modelos - Iris")

client = MlflowClient()
runs = client.search_runs(experiment_ids=["0"], order_by=["metrics.accuracy DESC"])

for run in runs:
    st.subheader(run.data.params["model"])
    st.write(f"Accuracy: {run.data.metrics['accuracy']:.2f}")