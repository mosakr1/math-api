FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cach-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]