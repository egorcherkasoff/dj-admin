#!/bin/bash
set -o errexit
set -o pipefail
set -o nounset
python adminka/manage.py collectstatic --noinput
python adminka/manage.py makemigrations
python adminka/manage.py migrate
python adminka/manage.py runserver 0.0.0.0:8000