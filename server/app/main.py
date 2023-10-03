from fastapi import FastAPI
from .scraper.scrape import scrape_all_restaurants
import json
from apscheduler.schedulers.background import BackgroundScheduler

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

@app.on_event("startup")
def init_job():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_all_restaurants, 'cron', hour=1)
    scheduler.start()




    