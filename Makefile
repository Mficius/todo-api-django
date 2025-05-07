# install-dev:
# 	docker compose exec web pre-commit install

# lint:
# 	docker compose exec web pre-commit run --all-files

# flake8:
# 	docker compose exec web flake8 .

flake8:
	docker compose exec web flake8 .

test:
	docker compose run --rm web python manage.py test
