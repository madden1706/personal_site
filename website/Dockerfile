FROM python:3.8.3-slim-buster

ENV PYTHONUNBUFFERED 1

COPY ./entrypoint.sh /opt/entrypoint.sh
COPY ./requirements.txt /opt/requirements.txt

COPY ./madresearchden/ /opt/madresearchden/
WORKDIR /opt/madresearchden/

RUN useradd mrd
RUN chown -R mrd /opt/madresearchden/
RUN pip install -r /opt/requirements.txt && apt-get update && apt-get install netcat -y
USER mrd

EXPOSE 8000
