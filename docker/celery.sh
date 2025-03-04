#!/bin/bash

if [[ "${1}" == "celery" ]]; then
    celery --app=app.tasks.celery:celery worker -l INFO
else [[ "${1}" == "flower" ]]; then
    celery --app=app.tasks.celery:celery flower
fi