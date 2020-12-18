python manage.py collectstatic --no-input

python manage.py migrate

gunicorn --worker-tmp-dir /dev/shm djcrm.wsgi