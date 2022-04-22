FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1  #Recommended  when running Python within Docker containers. Doesnt allow Python to buffer the outputs.

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app app

RUN adduser -D user #Make sure the app is not run by the root account for satefy
USER user