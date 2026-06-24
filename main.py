from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root(request: Request):
    return {
        "request.client.host": request.client.host,
        "ip": request.headers.get("X-Forwarded-For"),
    }
