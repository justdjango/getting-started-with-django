#!/usr/bin/env bash

set -o errexit

sudo apt install python3-pip

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
