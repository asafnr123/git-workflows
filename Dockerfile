FROM python3.12

WORKDIR app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY car.py .

CMD ["python3","app.py"]
