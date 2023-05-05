# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Run locally:
# CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
# ARG PORT=5000

# Run on cloud:
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
