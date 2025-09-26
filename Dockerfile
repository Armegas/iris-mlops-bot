FROM python:3.9-slim

WORKDIR /app

# Instala dependencias del sistema necesarias para pendulum y otros
RUN apt-get update && apt-get install -y build-essential libffi-dev && \
    rm -rf /var/lib/apt/lists/*

# Copia tu proyecto
COPY . .

# Actualiza pip y instala dependencias
RUN pip install --upgrade pip && \
    pip install "prefect==2.14.0" && \
    pip install -r requirements.txt

# Comando por defecto: lanza Streamlit
CMD ["streamlit", "run", "streamlit_dashboard/app.py"]
