FROM python:3.13

WORKDIR /app

COPY . /app

CMD ["python", "main.py"]
