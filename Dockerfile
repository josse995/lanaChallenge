FROM python:3.8.5-alpine

#Run in unbuffered mode when run in docker.
#Does not allow python to buffer the output
ENV PYTHONUNBUFFERED 1

#Install all the python dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
  gcc libc-dev linux-headers postgresql-dev musl-dev \
  zlib zlib-dev
RUN pip install -r /requirements.txt

RUN apk del .tmp-build-deps

#Create app folder and set as default folder
RUN mkdir /app
WORKDIR /app
COPY ./app /app

#Create a user for running applications only and switch to the user
#This mitigate security gaps (Running container with root is not good)
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user