from fastapi import FastAPI
from dotenv import load_dotenv
import os, requests
from datetime import datetime

load_dotenv()
app = FastAPI()

API_KEY = os.getenv("TIDE_API_KEY")
BASE_URL = "https://www.worldtides.info/api/v3"

# Hardcoded location (This serves as your base location)
LAT = 51.9500
LON = -7.8500

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tide Info API"}

@app.get("/tides")
def get_fixed_tide_data():
    try:
        # Step 1: Get nearby stations within a 50km radius using the stations endpoint
        station_resp = requests.get(BASE_URL, params={
            "stations": "",
            "lat": LAT,
            "lon": LON,
            "stationDistance": 50,
            "key": API_KEY
        })
        station_resp.raise_for_status()
        station_data = station_resp.json().get("stations", [])[:3]

        results = []

        # Step 2: Get tide data for each station using the extremes endpoint
        for station in station_data:
            extreme_resp = requests.get(BASE_URL, params={
                "extremes": "",
                "lat": station["lat"],
                "lon": station["lon"],
                "date": "today",
                "key": API_KEY
            })
            extreme_resp.raise_for_status()
            tide_data = extreme_resp.json().get("extremes", [])

        # Step 3: Format tide data

            tides = [
                {
                    "time": datetime.strptime(t["date"], "%Y-%m-%dT%H:%M%z").strftime("%H:%M"), # Make the date readable
                    "type": t["type"],                                                          # High or Low tide
                    "height": round(t["height"], 2)                                             # Round the tide to two decimal places
                }
                for t in tide_data
            ]
       # Step 4: Add tide and station data together 
            results.append({
                "station": station["name"],
                "location": f"{station['lat']}, {station['lon']}",
                "tides": tides
            })

        return {"tide_data": results}

    except requests.RequestException as e:
        return {"error": f"API call failed: {str(e)}"}
