FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update \
    && apt install -y --no-install-recommends gcc libpq-dev python-dev \
    && rm -rf /var/lib/apt/lists/*;

WORKDIR /code

ADD /code/requirements/ /tmp/

RUN pip install -U pip && pip install --no-cache-dir -r /tmp/develop.txt
