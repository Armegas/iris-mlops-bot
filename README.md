# 🧠 Iris MLflow Bot

![CI](https://github.com/Armegas/iris-mlops-bot/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.9-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Streamlit](https://img.shields.io/badge/streamlit-deployed-brightgreen)
[![HuggingFace Spaces](https://img.shields.io/badge/HuggingFace-Spaces-yellow)](https://huggingface.co/spaces/Armegas/iris-mlflow-bot)

Proyecto reproducible para entrenar modelos con el dataset Iris, registrar experimentos con MLflow, visualizar resultados con Streamlit, desplegar una API con FastAPI y evaluar el aprendizaje con quizzes adaptativos.

## 🚀 Instalación

```bash
git clone https://github.com/Armegas/iris-mlops-bot.git
cd iris-mlops-bot
bash setup.sh
```

## 🧪 Entrenamiento

```bash
python mlflow_tracking/train_models.py
```

## 📊 Dashboard

```bash
streamlit run streamlit_dashboard/app.py
```

## 🚀 API

```bash
uvicorn fastapi_service.main:app --reload
```

## 📘 Quiz

Disponible en `quizzes/`[`quiz.json`](https://quiz.json)

## 🐳 Docker

```bash
docker-compose up --build
```