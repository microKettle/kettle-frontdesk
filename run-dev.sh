#!/bin/bash
export FLASK_DEBUG=1
export FLASK_APP=app/__init__.py

export MONGODB_DB="kettle_dev"
export MONGODB_HOST="$(docker-machine ip)"

export REDIS_URL="redis://$(docker-machine ip)"

flask run
