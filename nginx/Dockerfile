FROM nginx:1.17.2

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY config/ /etc/nginx/
# Needed for certbot
RUN mkdir -p /.well-known/acme-challenge/
# COPY entrypoint.sh /entrypoint.sh
# ENTRYPOINT ["/entrypoint.sh"]

#https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#production-dockerfile