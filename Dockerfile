FROM python:3.8.5-slim-buster

# RUN apt-get update && apt-get install build-essential -y

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_DEBUG 0

ENV FLASK_APP flaskr
ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE 8000

CMD ["uwsgi", "--http", "0.0.0.0:8000", "--master", "-p", "4", "-w", "wsgi:app"]
