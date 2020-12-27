FROM python:3.8.7-slim-buster

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

RUN mkdir -p /opt/plots/
COPY ./plots/ /opt/plots/
WORKDIR /opt/plots/

