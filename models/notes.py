from pydantic import BaseModel

class Notes(BaseModel):
    title: str
    description: str
    completed: bool