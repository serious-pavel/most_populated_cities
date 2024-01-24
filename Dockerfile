FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

# Set Workdir
WORKDIR /app

# Copy files
COPY . /app

# Install requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Prepare application
RUN chmod +x /app/manage.py
RUN ./manage.py migrate
RUN ./manage.py update_or_create_countries
RUN ./manage.py update_or_create_cities
RUN ./manage.py collectstatic --noinput

# Run Application
CMD gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
