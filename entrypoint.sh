#!bin/sh
python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn --chdir techyroom --bind :8080 techyroom.wsgi:application