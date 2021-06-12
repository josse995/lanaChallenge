FROM python:3.8-slim-buster

#Run in unbuffered mode when run in docker.
#Does not allow python to buffer the output
ENV PYTHONUNBUFFERED 1

#Install all the python dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

#Create app folder and set as default folder
RUN mkdir /app
WORKDIR /app
COPY ./app /app/

ENV PYTHONPATH /app