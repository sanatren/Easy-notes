from fastapi import FastAPI
from routes.note import note
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.include_router(note)
if __name__ == "__main__":
    uvicorn.run("index:app", reload=True)
