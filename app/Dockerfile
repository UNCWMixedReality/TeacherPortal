FROM python:3.9.5-slim-buster

# Set working directory for all following in container commands
WORKDIR /usr/src/app

RUN apt-get update \
  && apt-get -y install gcc postgresql vim libpq-dev \
  && apt-get clean

# Handle all necessary dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEPLOYED 0

# Install App
COPY . .

# Queue any migrations
RUN python manage.py makemigrations