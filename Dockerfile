# Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY Mgtsys.py .

CMD ["python", "Mgtsys.py"]
