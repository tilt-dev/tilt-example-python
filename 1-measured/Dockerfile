FROM python:3.6

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/app/app.py"]
