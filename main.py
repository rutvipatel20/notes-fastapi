from fastapi import FastAPI
from routes.notes import notes

app = FastAPI()

app.include_router(notes)