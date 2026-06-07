## Run

1. Create the environment file and fill in `SECRET_KEY` and `POSTGRES_PASSWORD`:

   ```bash
   cp .env.example .env
   ```

2. Build and start:

   ```bash
   docker compose up --build
   ```

   The API is available at `http://localhost:8000`.

## API documentation

   Swagger UI — `http://localhost:8000/api/docs/`

## Migrations

Migrations run automatically on `web` startup. To run them manually:

```bash
docker compose run --rm web python manage.py migrate
```
