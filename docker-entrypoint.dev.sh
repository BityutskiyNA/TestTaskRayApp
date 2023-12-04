#!/bin/bash

while ! nc -z postgres 5432; do
  echo "Waiting for postgres..."
  sleep 1
done
echo "PostgreSQL started"

python manage.py migrate --no-input

python3 manage.py collectstatic --noinput

python3 manage.py runserver 0.0.0.0:8000

exec "$@"



