from fastapi import FastAPI
from datetime import datetime # func timeNow()
from zoneinfo import ZoneInfo # func timeNow()


from pydantic import BaseModel

app = FastAPI()

# Para hacer que el metodo sea un endpoint, se utiliza el decorador  (@app.get("/"))

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Bussines Rule: Colombian timezone
country_timezone = {
    "CO": "America/Bogota",
}

@app.get("/timeNow/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezone.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return{"time": datetime.now(tz)}


# model

class Customer(BaseModel):
    name = str
    description: str | None # pipe operator ( "|" ) allows to set the type as optional (None) or str
    