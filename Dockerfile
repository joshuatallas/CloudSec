FROM python:3.10.12

WORKDIR /app

COPY requirements.txt .
RUN pip install Flask==3.0.3

COPY requirements.txt . 
COPY app.py .

COPY . .

EXPOSE 5000

CMD ["python3", "app.py", "flask". "run", "host=0.0.0.0","--port=5000]







