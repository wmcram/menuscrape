from fastapi import FastAPI
from ..scraper.scrape import scrape_all_restaurants
import json
import time
import schedule

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.get("/menus/")
async def get_hall(hall: str, day: str):
    path = f"../scraper/data/{day}"
    with open(path, 'r') as f:
        data = json.load(path)
    return data

schedule.every(1).day.at("1:00").do(scrape_all_restaurants)


    