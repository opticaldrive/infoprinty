from fastapi import FastAPI, Request
from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates


app = FastAPI()


templates = Jinja2Templates(
    directory="templates/"
)  

@app.get("/")
def get_homepage(request: Request): 
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request.client.host": request.client.host,
            "ip": request.headers.get("X-Forwarded-For"),
            "headers": request.headers,
            "cookies": request.cookies
        },
    )

@app.get("/headers")
def get_headers(request: Request):  
    return request.headers

@app.get("/cookies")
def get_headers(request: Request):  
    return request.cookies




