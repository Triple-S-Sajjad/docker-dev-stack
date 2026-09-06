# Docker Dev Stack

A containerized web application built with Flask and PostgreSQL, orchestrated with Docker Compose.

## Tech Stack

- **Python / Flask** — REST API
- **PostgreSQL 15** — Database
- **Docker & Docker Compose** — Containerization

## Architecture

```
Flask App (Port 5000)  →  PostgreSQL DB (Port 5432)
        ↕
  Docker Network (docker-compose)
```
## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Run Locally

1. Clone the repo
```bash
   git clone https://github.com/Triple-S-Sajjad/docker-dev-stack.git
   cd docker-dev-stack
```

2. Create a `.env` file from the provided example and edit the values
```bash
   cp .env.example .env
```
The `.env` file is gitignored and is required by `docker-compose.yml`. It must define:
```bash
   DB_HOST=db
   DB_NAME=devstack
   DB_USER=youruser
   DB_PASSWORD=changeme
```
`DB_HOST` must be `db` — the name of the Postgres service in `docker-compose.yml`.

3. Start the containers
```bash
   docker-compose up --build
```

4. Verify it is running
```bash
   curl http://localhost:5000/          # {"message": "Docker Dev Stack is running!"}
   curl http://localhost:5000/health    # {"status": "healthy", "database": "connected"}
```

### Running the tests

The test suite exercises a real database. Point the `DB_*` variables at a
running Postgres instance and run pytest:
```bash
   DB_HOST=localhost DB_NAME=devstack DB_USER=youruser DB_PASSWORD=changeme \
     pytest app/tests/
```
CI runs these same tests against a `postgres:15` service on every push to `master`.

## API Endpoints

| Method | Endpoint  | Description              |
|--------|-----------|--------------------------|
| GET    | `/`       | Returns running status   |
| GET    | `/health` | Checks database connection |

## What I Learned

- Writing Dockerfiles and containerizing a Python app
- Networking between containers with Docker Compose
- Managing environment variables and secrets
- Health checking a live database connection
