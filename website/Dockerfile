# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /website

# Set the working directory to /music_service
WORKDIR /website

# Copy the current directory contents into the container at /music_service
ADD . /website

COPY ./entrypoint.sh /entrypoint.sh
# Install any needed packages specified in requirements.txt

# Needed for script that checks that the db is up.
RUN pip install -r requirements.txt 
RUN apt-get update
RUN apt-get install netcat -y

# ENTRYPOINT ["/entrypoint.sh"]
