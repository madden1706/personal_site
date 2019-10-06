FROM nginx:1.17.2

RUN rm /etc/nginx/conf.d/default.conf
COPY ./conf.d/ /etc/nginx/conf.d/

#https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#production-dockerfile