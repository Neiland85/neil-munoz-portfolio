from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse


router = APIRouter()
templates = Jinja2Templates(directory="src/app/templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse(
        request,
        "index.html",
        {},
    )
