POETRY = docker exec app poetry run

run:
	docker compose --env-file ./env/.env up -d

build:
	docker compose --env-file ./env/.env build

req_install:
	$(POETRY) poetry install

logs:
	docker logs app -f

stop:
	docker stop $$(docker ps -a -q)

migration:
	$(POETRY) alembic revision --autogenerate

migrate:
	$(POETRY) alembic upgrade head