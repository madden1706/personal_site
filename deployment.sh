# Deployment script.
# This assumes the awsebcli is installed in the env.
# Use from the home folder of the project. 

eb init;
mkdir .ebextensions;
touch .ebextensions/django.config;
echo "option_settings: ""
  aws:elasticbeanstalk:container:python:
    WSGIPath: ebdjango/wsgi.py" >> .ebextensions/django.config # update path to wsgi.py.

# Create the eb env
eb create django-env; # Update the name of the env. 

# Update the allowed hosts

# You can set environment variables for your running environment at any time by typing the following:
#     eb setenv foo=bar

#/opt/python/run/venv/bin/pip install -r /opt/python/ondeck/app/requirements.txt





