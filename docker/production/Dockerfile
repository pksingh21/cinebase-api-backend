FROM python:3.10-bullseye

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y --no-install-recommends libpq5 libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN set -eu \
    && pip install --no-cache-dir -r requirements.txt uvicorn

RUN apt-get update \
    && apt-get purge -y --no-install-recommends libpq-dev \
    && apt-get autopurge -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY . .

COPY ./docker/production/docker-entrypoint.sh /

ENV CINEBASE_DEBUG=0

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["python", "-m", "uvicorn", "--host", "0.0.0.0", "cinebase_api.asgi:application"]
