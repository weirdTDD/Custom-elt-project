# Data Engineering ELT

Small Docker-based ELT sandbox with:

- a source PostgreSQL database
- a destination PostgreSQL database
- seed data for the source database
- a placeholder Python ETL/ELT script

## Project Layout

- `docker-compose.yaml`: defines the source DB, destination DB, and ETL container
- `source_db_init/init.sql`: creates and seeds the source database
- `elt/script.py`: placeholder for the pipeline logic
- `Dockerfile`: Python image for running the ETL script

## What It Does Today

The source database is initialized with sample tables and data for:

- `users`
- `films`
- `film_category`
- `actors`
- `film_actors`

The destination database is started, but no transformation/load logic is implemented yet because [`elt/script.py`](/home/it_weirdtdd/projects/data-enginerring-elt/elt/script.py) is currently empty.

## Run

Start the stack with:

```bash
docker compose up --build
```

Source Postgres is exposed on `localhost:5433`.

Destination Postgres is exposed on `localhost:5434`.

Current credentials in [`docker-compose.yaml`](/home/it_weirdtdd/projects/data-enginerring-elt/docker-compose.yaml):

- database: `source_db` / `destination_db`
- user: `postgres`
- password: `secret`

## Connect

Example connection commands:

```bash
psql -h localhost -p 5433 -U postgres -d source_db
psql -h localhost -p 5434 -U postgres -d destination_db
```

## Notes

This repo looks like a work in progress. Before this is production-ready, the next likely steps are:

- implement [`elt/script.py`](/home/it_weirdtdd/projects/data-enginerring-elt/elt/script.py)
- fix the Compose/Docker wiring for the ETL container
- define the destination schema and load process
