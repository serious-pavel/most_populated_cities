./manage.py migrate
./manage.py update_or_create_countries
./manage.py update_or_create_cities
./manage.py collectstatic --noinput
gunicorn.exe most_populated_cities.wsgi:application --bind 0.0.0.0:8080
#./manage.py runserver 0.0.0.0:8080 --nostatic