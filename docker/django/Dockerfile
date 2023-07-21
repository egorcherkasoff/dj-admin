FROM python:3.11.1-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && apt-get install -y build-essential libpq-dev

WORKDIR /app

COPY ./requirements.txt .

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# django run
COPY ./docker/django/start.sh /start

RUN sed -i 's/\r$//' /start

RUN chmod +x /start