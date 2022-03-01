
# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /main

RUN pip install pygame

COPY . .

CMD [ "python3", "-m" , "run", "--host=0.0.0.0"]
