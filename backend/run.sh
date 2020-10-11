#!/usr/bin/env bash

python ./manage.py collectstatic --noinput

uvicorn starwars.asgi:application --host 0.0.0.0 --reload
