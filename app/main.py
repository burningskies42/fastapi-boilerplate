from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routers import accordion, twoforms, unsplash

from .library.helpers import open_file

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(unsplash.router)
app.include_router(twoforms.router)
app.include_router(accordion.router)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = open_file("home.md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = open_file(page_name + ".md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})
