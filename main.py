from fastapi import FastAPI
from app.core.database import Base , engine
from app.models import User, Task
from app.routes import task , user

app = FastAPI(title="TaskFlow API")

# create tables
Base.metadata.create_all(bind=engine)
app.include_router(user.router)
app.include_router(task.router)


@app.get("/")
def root():
    return {"message": "Tables created"}