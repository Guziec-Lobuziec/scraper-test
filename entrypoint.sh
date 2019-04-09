#!/bin/bash

python manage.py makemigrations

python manage.py migrate

crontab cron_jobs.txt

bash crawl.sh &

python manage.py runserver 0.0.0.0:8000
