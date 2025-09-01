FROM python:3.11-slim

WORKDIR /app

COPY checkTemp.py .

CMD ["python3", "checkTemp.py"]
