#!/bin/sh
set -e

rm  -f ./db.sqlite3

python manage.py migrate

python manage.py loaddata \
    auth_admin
