#!/bin/bash
set -eu

readonly cinebase_user="${CINEBASE_PG_USER:-cinebase_user}"
readonly cinebase_password="${CINEBASE_PG_PASSWORD}"
readonly cinebase_db="${CINEBASE_DB:-cinebase}"

psql -v ON_ERROR_STOP=1 --username "${POSTGRES_USER}" --dbname "${POSTGRES_DB}" <<-EOSQL
	CREATE USER ${cinebase_user} WITH PASSWORD '${cinebase_password}';
	CREATE DATABASE ${cinebase_db};
	GRANT ALL PRIVILEGES ON DATABASE ${cinebase_db} TO ${cinebase_user};
EOSQL

psql -v ON_ERROR_STOP=1 --username "${POSTGRES_USER}" --dbname "${CINEBASE_DB}" <<-EOSQL
        GRANT ALL PRIVILEGES ON SCHEMA public TO ${cinebase_user};
EOSQL
