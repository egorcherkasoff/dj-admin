# Dj Admin

## Overview

This project is an example of admin panel for company working with products orders and shipments.

## Features
todo

## Installation

You can install this project with Docker / docker-compose or manually.

### Docker / docker-compose Installation

Make sure you have docker and docker-compose installed

Create a .env file in the root directory of the project and specify following environment variables:

```
MYSQL_HOST="db"
MYSQL_PORT="3306"
MYSQL_USER="your database user"
MYSQL_PASSWORD="your database password"
MYSQL_DATABASE="database name"
MYSQL_ROOT_PASSWORD="mysql root password"
SECRET_KEY="django app secret key"

EMAIL_HOST = "email host"
EMAIL_PORT = email port
EMAIL_HOST_USER = "email that will send emails"
EMAIL_HOST_PASSWORD = "mail app password"
```

For example:

```
MYSQL_HOST="db"
MYSQL_PORT="3306"
MYSQL_USER="root"
MYSQL_PASSWORD="root"
MYSQL_DATABASE="adminka"
MYSQL_ROOT_PASSWORD="rootpass"
SECRET_KEY="mysupersecretkey"

EMAIL_HOST = "smtp.yandex.ru"
EMAIL_PORT = 465
EMAIL_HOST_USER = "adminka.emails@yandex.ru"
EMAIL_HOST_PASSWORD = "mymailapppasswd"
```

Then run the following command:

`docker-compose build && docker-compose up`

or

`make build`

If you have Chocolatey with support of Makefile installed 

Then open your browser and go to [http://localhost:80](http://localhost:80)

To create superuser run:

`docker exec -it adminka-app python /app/manage.py createsuperuser`

or

`make createsuperuser`

### Manual Installation

Clone this Git repository:

`git clone https://github.com/egorcherkasoff/dj-admin`

Install dependencies:

`pip install -r requirements.txt`

Create a .env file in the root directory of the project and specify following environment variables:

```
MYSQL_HOST="your database host"
MYSQL_PORT="your database port"
MYSQL_USER="your database user"
MYSQL_PASSWORD="your database password"
MYSQL_DATABASE="database name"
MYSQL_ROOT_PASSWORD="mysql root password"
SECRET_KEY="django app secret key"

EMAIL_HOST = "email host"
EMAIL_PORT = email port
EMAIL_HOST_USER = "email that will send emails"
EMAIL_HOST_PASSWORD = "mail app password"
```

For example:

```
MYSQL_HOST="localhost"
MYSQL_PORT="3306"
MYSQL_USER="root"
MYSQL_PASSWORD="root"
MYSQL_DATABASE="adminka"
MYSQL_ROOT_PASSWORD="rootpass"
SECRET_KEY="mysupersecretkey"

EMAIL_HOST = "smtp.yandex.ru"
EMAIL_PORT = 465
EMAIL_HOST_USER = "adminka.emails@yandex.ru"
EMAIL_HOST_PASSWORD = "mymailapppasswd"
```

Create superuser:

`python adminka/manage.py createsuperuser`

Run the app:

`python adminka/manage.py runserver`

Then open your browser and go to [http://localhost:8000](http://localhost:8000) 


## Usage

todo

## To do

- add orders management
- finish shipment management
- finish this readme
- fix bugs
- add mobile reponsiveness
- refactor code

## Contributing 

If you find a bug or have an idea for a new feature, please create an issue or pull request in this repository.
