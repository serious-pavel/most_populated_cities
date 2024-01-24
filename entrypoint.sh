./manage.py migrate
./manage.py update_or_create_countries
./manage.py update_or_create_cities
./manage.py collectstatic --noinput
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000