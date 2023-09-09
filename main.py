# main.py
# to start: uvicorn main:app --reload

import helpers.time as time
from fastapi import FastAPI

app = FastAPI()


@app.get("/api")
async def information():
    info = {
        "Docs": "Checkout the doc of this API here http://127.0.0.1:8000/docs/",
        "GitHub": "https://github.com/MJerich/reigns-secret-api"
    }
    return info


@app.get("/api/time")
async def get_current_time():
    current_time = time.current_time_request()
    return current_time


@app.get("/api/year")
async def get_current_year():
    current_year = time.current_year_request()
    return current_year
