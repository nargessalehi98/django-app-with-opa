FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /django-app-with-opa

COPY ./requirements.txt /django-app-with-opa
WORKDIR /django-app-with-opa

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --bind  0.0.0.0:$PORT --workers $WORKER  config.wsgi:application
