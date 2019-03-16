FROM python:3.7.2-alpine3.7

# Install system dependencies.
RUN apk update && \
    apk add  --no-cache \
    bash gcc python3-dev musl-dev postgresql-dev

WORKDIR /app

# Add requirements and install.
ADD ./requirements-dev.txt ./requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements-dev.txt

# Add application source.
ADD . /app/

CMD ["/app/entrypoint.sh"]
