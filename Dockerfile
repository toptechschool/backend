FROM python:3.9.6-alpine
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

RUN addgroup app && adduser -S app -G app
RUN mkdir /app && chown app:app /app

USER app

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .