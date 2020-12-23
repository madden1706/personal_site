#!/bin/sh  
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z postgres $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
# ----- This will remove all db data!!!!! ------
# python manage.py flush --no-input

exec "$@"
                              