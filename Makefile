build:
	docker-compose build && docker-compose up

down:
	docker-compose down

createsuperuser:
	docker exec -it adminka-app python /app/adminka/manage.py createsuperuser

migrate:
	python adminka/manage.py makemigrations && python adminka/manage.py migrate

local:
	python adminka/manage.py runserver