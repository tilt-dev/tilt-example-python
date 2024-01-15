FROM python:3-alpine

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/app/app.py"]
