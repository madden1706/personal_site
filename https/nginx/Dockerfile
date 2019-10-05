FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

RUN mkdir /var/www/certbot

RUN mkdir /usr/share/nginx/
COPY index.html /usr/share/nginx/

#  Docker-comp file to run certbot
# cron job to update. 

#  link volumes