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

FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /use/src/app
WORKDIR /use/src/app

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .