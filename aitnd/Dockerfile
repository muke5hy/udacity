FROM python:3.6-alpine

WORKDIR /
COPY . ./

RUN apk --update add --virtual build-dependencies openssl ca-certificates py-openssl wget \
    libffi-dev openssl-dev python-dev py-pip build-base  gfortran

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apk del build-dependencies