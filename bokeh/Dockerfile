FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /opt/bokeh_apps/
WORKDIR /opt/bokeh_apps/
COPY . /opt/bokeh_apps/

RUN pip install -r requirements.txt

