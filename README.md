uv add psycopg2-binary
uv add sqlalchemy
uv pip install gunicorn
 uv run alembic upgrade head
 uv run alembic init alembic
  uv alembic revision --autogenerate -m "update smart task managements table"