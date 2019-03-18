#!/usr/bin/env bash

set -ev

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )


# Setup the db (create tables, seed db and create test database).
python -m endex.utils.setupdb


# Run server.
gunicorn --workers 4 --reload --bind 0.0.0.0:8000 'endex.app:get_app()'
