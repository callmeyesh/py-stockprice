FROM python:3.10.6-alpine3.15

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.2.0

WORKDIR /app

RUN apk add --no-cache gcc libffi-dev musl-dev make
RUN pip install "poetry==$POETRY_VERSION"

COPY . /app/
RUN cd /app/ && make install
