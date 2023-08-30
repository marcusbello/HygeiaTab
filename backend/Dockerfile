FROM python:3.10.6-buster

RUN apt-get update

COPY . /src 
WORKDIR /src

RUN make env

ENV IS_CI=true