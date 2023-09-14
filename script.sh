#!/bin/bash
sleep 8

python manage.py migrate
python manage.py runserver 0.0.0.0:8000