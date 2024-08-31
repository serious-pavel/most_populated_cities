FROM python:3.12-slim

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
RUN chmod +x /app/entrypoint.sh

# Run Application
CMD /bin/sh -c "./entrypoint.sh"
