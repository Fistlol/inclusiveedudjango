FROM python:3.8.10-slim-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt update \
    && apt clean

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

VOLUME ["/cachedir"]

EXPOSE 8000

LABEL SERVICE_NAME="own_django"
LABEL SERVICE_TAGS="django"