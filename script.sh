#!/bin/bash
python manage.py createsuperuser \
    --username=admin \
    --email=admin@example.com \
    --noinput
python manage.py migrate
python manage.py runserver 0.0.0.0:8000