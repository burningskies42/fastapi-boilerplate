import os

from dotenv import load_dotenv
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from loguru import logger

load_dotenv()

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("/unsplash", response_class=HTMLResponse)
async def unsplash_home(request: Request):
    key = os.getenv("unsplash_key")
    logger.info(f"secret key is: {key}")
    return templates.TemplateResponse("unsplash.html", {"request": request})
