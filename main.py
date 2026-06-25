from fastapi import FastAPI, Request

app = FastAPI()


# @app.get("/")
# async def root(request: Request):
#     return {
#         "request.client.host": request.client.host,
#         "ip": request.headers.get("X-Forwarded-For"),
#     }

from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates


# https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-apirouter

router = APIRouter(tags=["pages"])

templates = Jinja2Templates(
    directory="templates/"
)  # todo -  move everything to template


@app.get("/")
def get_homepage(request: Request):  # sync = runs in threadpool,
    # so its blocking DB work never stalls the event loop (matters under HN-spike load)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request.client.host": request.client.host,
            "ip": request.headers.get("X-Forwarded-For"),
        },
    )


# ui views tbd
