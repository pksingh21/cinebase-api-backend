#!/bin/bash
set -eu

echo "Apply database migrations..."
python manage.py migrate

exec "$@"
