# Docker Dev Stack

A containerized web application built with Flask and PostgreSQL, orchestrated with Docker Compose.

## Tech Stack

- **Python / Flask** — REST API
- **PostgreSQL 15** — Database
- **Docker & Docker Compose** — Containerization

## Architecture
┌─────────────────┐     ┌─────────────────┐
│   Flask App     │────▶│   PostgreSQL    │
│   Port 5000     │     │   Port 5432     │
└─────────────────┘     └─────────────────┘
│
Docker Network
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

2. Create a `.env` file
DB_HOST=db
DB_NAME=devstack
DB_USER=youruser
DB_PASSWORD=yourpassword
3. Start the containers
```bash
   docker-compose up --build
```

## API Endpoints

| Method | Endpoint  | Description              |
|--------|-----------|--------------------------|
| GET    | `/`       | Returns running status   |
| GET    | `/health` | Checks database connection |

## What I Learned

- Writing Dockerfiles and multi-stage builds
- Networking between containers with Docker Compose
- Managing environment variables and secrets
- Health checking a live database connection
