FROM python:3.9-slim-buster
LABEL maintainer="tarek5701@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG APP_HOME=/app
WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install --no-install-recommends -y build-essential libpq-dev

COPY ./compose/production/start /start
COPY ./requirements.txt .
RUN pip install -r requirements.txt && \
    sed -i 's/\r$//g' /start && \
    chmod +x /start && \
    addgroup --system app && adduser --system --ingroup app app &&\
    chmod -R +x /start

COPY . ${APP_HOME}

USER app

EXPOSE 8000