FROM postgres:10.1-alpine

COPY init/ /docker-entrypoint-initdb.d/

RUN mkdir -p /var/lib/postgresql/data/
