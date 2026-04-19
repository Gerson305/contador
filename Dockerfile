FROM python:3.13-slim  

WORKDIR /app

COPY . .

RUN pip install -r requirements-dev.txt

CMD ["python3","main.py"]
