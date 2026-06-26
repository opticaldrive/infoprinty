from fastapi import FastAPI, Request
from fastapi import Request, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import geoip2.database

city_reader = geoip2.database.Reader("geoip/GeoLite2-City.mmdb")
asn_reader  = geoip2.database.Reader("geoip/GeoLite2-ASN.mmdb")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(
    directory="templates/"
)  

@app.get("/")
def get_homepage(request: Request): 
    ip = request.headers.get("X-Forwarded-For")
    if ip == None:
        ip =  request.client.host
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request.client.host": request.client.host,
            "ip": ip, #request.headers.get("X-Forwarded-For"),
            "geo": geo_ip(ip),
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




@app.get("/json")
def get_info(request: Request):  
    xff = request.headers.get("X-Forwarded-For")
    ip = xff.split(",")[0].strip() if xff else request.client.host
    return geo_ip(ip)

def geo_ip(ip):
    try:
        city = city_reader.city(ip)
        asn  = asn_reader.asn(ip)
        geo = {
            "ip": ip,
            "country": city.country.name,
            "city": city.city.name,
            "lat": city.location.latitude,
            "lon": city.location.longitude,
            "asn": asn.autonomous_system_number,
            "org": asn.autonomous_system_organization,
        }
        return geo
    except (geoip2.errors.AddressNotFoundError, ValueError):
        geo = None
        return geo
   

