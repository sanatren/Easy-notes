def noteconverter(item) -> dict:
    return {
        "id" : item["id"],
        "title":item["title"],
        "description":item["description"],
        "important":item["important"],
    }
def notesEntity(items) -> list:
    return[noteconverter(item) for item in items]