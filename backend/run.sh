#!/usr/bin/env bash

python ./manage.py collectstatic

#gunicorn starwars.asgi:application -k uvicorn.workers.UvicornWorker
uvicorn starwars.asgi:application --host 0.0.0.0 --reload
