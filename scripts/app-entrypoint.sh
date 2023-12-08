#!/bin/sh

export $(grep -v '^#' ./env/.env | xargs)
poetry run uvicorn src.main:app --port=$APP_PORT --host=$APP_HOST --reload --log-level=info