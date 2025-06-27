from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TIDE_API_KEY")
API_URL = "https://api.tidesandcurrents.noaa.gov/api_endpoint"  # Replace with actual endpoint

app = FastAPI()

@app.get("/tides")
def get_tide_data():
    params = {
        "station": "8720218",
        "product": "predictions",
        "datum": "MLLW",
        "interval": "h",
        "units": "metric",
        "time_zone": "lst_ldt",
        "format": "json",
        "api_key": API_KEY,
    }
    try:
        res = requests.get(API_URL, params=params)
        return res.json()
    except Exception as e:
        return {"error": str(e)}
