include .env
export

install:
	pip install -e .

db:
	docker run -d --name tz_goodreads -p ${PG_DB_PORT}:5432 -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} -e POSTGRES_DB=${PG_DB_NAME} postgres

load_data:
	python -m bin.build_db

app:
	uvicorn transitionzero.goodreads.app:app