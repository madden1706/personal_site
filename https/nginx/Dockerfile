FROM nginx:1.17.2

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d

# RUN rm /usr/share/nginx/html/index.html
COPY ./index.html /usr/share/nginx/html/index.html

#  Docker-comp file to run certbot
# cron job to update. 

#  link volumes