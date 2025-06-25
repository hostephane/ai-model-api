FROM python:3.10-slim

WORKDIR /app

# Installe DVC
RUN pip install dvc[s3]

# Copie les fichiers requirements et le code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Récupère les données et modèles versionnés avec DVC
RUN dvc pull

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
