from fastapi import APIRouter, HTTPException
from models.notes import Notes
from config.db import conn
from schemas.notes import notesEntity, noteEntity

notes = APIRouter()

@notes.get("/", response_model=list[Notes])
async def read_notes():
    return notesEntity(conn.local.notes.find())

@notes.post("/", response_model=Notes)
async def add_notes(note: Notes):
    conn.local.notes.insert_one(dict(note))
    return note

@notes.put("/{id}", response_model=Notes)
async def update_notes(id: str, note: Notes):
    conn.local.notes.find_one_and_update({"_id": id}, {"$set": dict(note)})
    return note

@notes.delete("/{id}", response_model=Notes)
async def delete_notes(id: str):
    conn.local.notes.find_one_and_delete({"_id": id})
    return id