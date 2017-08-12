FROM python:2.7-alpine

RUN apk add --no-cache git

COPY . /app
WORKDIR /app
RUN pip install .
