
from pydantic import BaseModel
from typing import Optional
from sentence_predictor import predictor

class Note(BaseModel):
    Title: str
    description: str
    content: str
    important: Optional[bool] = False

    @staticmethod
    def predict_next_words(content: str, next_words: int = 3):
        return predictor.predict_next_words(content, next_words)

class NoteInDB(Note):
    id: str