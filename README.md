# TaskFlow API

A simple FastAPI project for user and task management with SQLAlchemy and PostgreSQL.

## Features

- Create and list users
- Create and list tasks
- SQLAlchemy ORM models with one-to-many relation (`User -> Task`)
- Environment-based database configuration
- Alembic migration setup included

## Tech Stack

- FastAPI
- SQLAlchemy
- PostgreSQL (`psycopg2-binary`)
- Pydantic
- Alembic

## Project Structure

```text
app/
  core/
    database.py
  models/
    user.py
    task.py
  routes/
    user.py
    task.py
  schemas/
    user.py
    task.py
  services/
    user.py
    task.py
main.py
```

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database>
```

4. Run the API:

```powershell
uvicorn main:app --reload
```

5. Open docs:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

- `GET /` - Health/root response
- `POST /users/` - Create a user
- `GET /users/` - List users
- `POST /tasks/` - Create a task
- `GET /tasks/` - List tasks

## Example Payloads

Create user (`POST /users/`):

```json
{
  "name": "Afzal",
  "email": "afzal@example.com"
}
```

Create task (`POST /tasks/`):

```json
{
  "title": "Finish API docs",
  "owner_id": 1
}
```

## Alembic (Optional)

Run migrations:

```powershell
alembic upgrade head
```

Create a new migration:

```powershell
alembic revision --autogenerate -m "describe_change"
```
