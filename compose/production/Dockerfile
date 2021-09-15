FROM python:3.9-slim-buster

RUN apt-get update && apt-get install --no-install-recommends -y build-essential libpq-dev

ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ${APP_HOME}

COPY ./compose/production/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

RUN addgroup --system app && adduser --system --ingroup app app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

USER app

COPY . ${APP_HOME}

EXPOSE 8000