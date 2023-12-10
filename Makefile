POETRY = docker exec app poetry run

run: # run docker containers
	docker compose --env-file ./env/.env up -d

build: # build docker containers
	docker compose --env-file ./env/.env build

req_install: # install requirements in app container
	$(POETRY) poetry install

logs: # show logs in app container
	docker logs app -f

stop: # stop all containers
	docker stop $$(docker ps -a -q)

migrations: # create migrations inside app container
	$(POETRY) alembic revision --autogenerate

migrate: # apply migration inside application container for database
	$(POETRY) alembic upgrade head