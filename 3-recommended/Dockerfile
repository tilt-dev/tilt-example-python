FROM python:3.6

# Default value; will be overridden by build-args, if passed
ARG flask_env=production

ENV FLASK_ENV $flask_env

WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .

ENTRYPOINT ["python", "/app/app.py"]
