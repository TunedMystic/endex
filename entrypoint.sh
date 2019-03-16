#!/usr/bin/env bash

set -ev

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )


# Create tables.


# Seed db.


# Run server.
gunicorn --workers 4 --reload --bind 0.0.0.0:8000 endex.app:app
