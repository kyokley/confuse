FROM python:3.5-alpine

RUN apk add --no-cache git

COPY . /app
WORKDIR /app
RUN python setup.py install
