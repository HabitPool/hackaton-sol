# Server solana hackaton

### First run

- `docker-compose up --build server` 🚀
- `docker-compose run --rm server flask --app backend:app db upgrade`

### DB Migrations

- Init: `docker-compose run --rm server flask --app backend:app db init`
- Create revision: `docker-compose run --rm server flask --app backend:app db migrate -m "<some message>"`
- Upgrade to latest revision: `docker-compose run --rm server flask --app backend:app db upgrade`

Using docker-compose services to update schema

- Migration: `docker-compose up --build migration`
- Upgrade: `docker-compose up --build upgrade`
