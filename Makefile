makemigrations-hello:
	docker-compose run --rm django_try python3 manage.py makemigrations hello

migrate:
	docker-compose run --rm django_try python3 manage.py migrate

createsuperuser:
	docker-compose run --rm django_try python3 manage.py createsuperuser

shell:
	docker-compose run --rm django_try python3 manage.py shell