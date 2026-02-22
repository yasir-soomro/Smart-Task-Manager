from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    owner_id: int

class TaskOut(BaseModel):
    id: int
    title: str
    status: str
    owner_id: int

    class Config:
        from_attributes = True