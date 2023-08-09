from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from scripts.ebay import ebay
import os

app = FastAPI()

templates = Jinja2Templates(directory=os.path.join(os.getcwd(), "templates"))

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process-query")
async def process_query(query: str = Form(...)):
    result = ebay(query)
    return {"message": f"Form data received: {result}"}