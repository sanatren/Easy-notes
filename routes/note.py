from fastapi import APIRouter, Request, HTTPException, Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from config.db import supa
from models.note import Note
import uuid
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_notes(request: Request):
    try:
        response = supa.table("Notes").select("*").execute()
        notes = []
        if response and response.data:
            for doc in response.data:
                notes.append({
                    "id": doc.get("id"),
                    "title": doc.get("Title"),
                    "content": doc.get("content"),
                    "description": doc.get("description"),
                    "important": doc.get("important")
                })
        return templates.TemplateResponse("index.html", {"request": request, "newDocs": notes})
    except Exception as e:
        print(f"Error in read_notes: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@note.post("/")
async def create_note(
        request: Request,
        Title: str = Form(...),
        description: str = Form(...),
        content: str = Form(...),
        important: bool = Form(False)
):
    try:
        note = Note(
            Title=Title,
            description=description,
            content=content,
            important=important
        )
        db_note = {**note.dict(), "id": str(uuid.uuid4())}
        response = supa.table("Notes").insert(db_note).execute()
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        print(f"Error in create_note: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@note.put("/update/{note_id}")
async def update_note(
        note_id: str,
        note: Note
):
    try:
        logger.info(f"Attempting to update note with ID: {note_id}")

        updated_note = {
            "Title": note.Title,
            "description": note.description,
            "content": note.content,
            "important": note.important
        }

        response = supa.table("Notes").update(updated_note).eq("id", note_id).execute()

        logger.info(f"Supabase response: {response}")

        if response.data:
            return JSONResponse(content={"message": "Note updated successfully", "data": response.data},
                                status_code=200)
        else:
            logger.warning(f"No data returned from Supabase for note ID: {note_id}")
            raise HTTPException(status_code=404, detail="Note not found or no changes made")
    except Exception as e:
        logger.error(f"Error in update_note: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@note.delete("/delete/{note_id}")
async def delete_note(note_id: str):
    try:
        response = supa.table("Notes").delete().eq("id", note_id).execute()
        if response.data:
            return {"message": "Note deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Note not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@note.post("/predict")
async def predict_next_words(request: Request):
    try:
        data = await request.json()
        content = data.get("content")
        next_words = data.get("next_words", 3)

        if not content:
            raise HTTPException(status_code=400, detail="Content cannot be empty")

        predicted_words = Note.predict_next_words(content, next_words)
        return JSONResponse(content={"predicted_words": predicted_words})
    except Exception as e:
        print(f"Error in predict_next_words: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))