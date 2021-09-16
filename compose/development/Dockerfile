FROM python:3.9-slim-buster
LABEL maintainer="tarek5701@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


ARG APP_HOME=/app
WORKDIR ${APP_HOME}

COPY ./requirements.txt .
COPY ./compose/development/start /start
COPY . ${APP_HOME}

RUN apt-get update && apt-get install --no-install-recommends -y build-essential libpq-dev &&\
    pip install -r requirements.txt &&\
    sed -i 's/\r$//g' /start &&\
    chmod +x /start &&\
    addgroup app && adduser --system --group app

USER app

EXPOSE 8000