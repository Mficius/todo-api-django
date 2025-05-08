.PHONY: test

flake8:
	docker compose exec web flake8 .

test:
	docker compose exec web pytest --disable-warnings -v

migrate:
	docker compose exec web python manage.py migrate
