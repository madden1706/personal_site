FROM postgres:10.1-alpine

RUN mkdir -p /var/lib/postgresql/data/

COPY ./entrypoint.sh /docker-entrypoint-initdb.d/entrypoint.sh

ENTRYPOINT ["/docker-entrypoint-initdb.d/entrypoint.sh"]
