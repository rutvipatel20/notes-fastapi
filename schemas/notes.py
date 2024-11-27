def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "description": item["description"],
        "completed": item["completed"]
    }

def notesEntity(entity) -> list:
    return [noteEntity(i) for i in entity]