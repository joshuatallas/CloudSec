FROM python:3.10.12

WORKDIR /app

RUN pip install Flask==3.0.0 psycopg[binary]==3.1.18

COPY requirements.txt .
COPY app.py .
COPY create_table.sql .

EXPOSE 5000

CMD ["python3", "app.py"]







