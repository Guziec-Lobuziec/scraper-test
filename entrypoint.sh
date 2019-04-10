#!/bin/bash
#scraper start
python manage.py migrate

crontab cron-jobs.txt

bash crawl.sh &

python manage.py runserver 0.0.0.0:8000
