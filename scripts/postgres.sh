#!/usr/bin/env bash

set -e

# Create volume.
docker volume create pg_data


# Remove postgres container.
docker rm -f pg || true


# Run postgres container.
docker \
    run -d \
    --name pg \
    --publish 5432:5432 \
    --mount source=pg_data,target=/var/lib/postgresql/data \
    postgres:11.2-alpine
