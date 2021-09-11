# FROM python:3.4
# ENV PYTHONUNBUFFERED=1
# ENV PYTHONDONTWRITEBYTECODE 1

# RUN addgroup app && adduser -S app -G app
# RUN mkdir /app && chown app:app /app

# USER app

# # WORKDIR /usr/src/app
# WORKDIR /app


# COPY ./requirements.txt .

# RUN pip install -r requirements.txt

# COPY . .


# FROM python:3.6

# ENV PYTHONUNBUFFERED 1

# RUN addgroup app && adduser --system --group app
# RUN mkdir /usr/src/app && chown app:app /usr/src/app
# USER app
# WORKDIR /usr/src/app

# COPY ./requirements.txt .
# RUN pip install -r requirements.txt
# COPY . .

ARG PYTHON_VERSION=3.9-slim-buster
FROM python:${PYTHON_VERSION} as python

RUN apt-get update && apt-get install --no-install-recommends -y build-essential libpq-dev

ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ${APP_HOME}

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./compose/development/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY . ${APP_HOME}