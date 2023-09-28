import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url_prefix = "https://wisc-housingdining.nutrislice.com/menu"

def scrape_menu(url):
    browser.get(url)
    browser.implicitly_wait(5)
    btn = browser.find_elements(By.XPATH,'//button[text()="View Menus"]')
    if btn:
        btn[0].click()
        browser.implicitly_wait(5)

    menu = browser.find_elements(By.CLASS_NAME, "menu-container")
    if not menu: return {}
    restaurants = menu[0].find_elements(By.TAG_NAME, "ns-menu-section")

    data = []
    for restaurant in restaurants:
        restaurant_data = {}
        restaurant_data["restaurant_title"] = restaurant.find_element(By.TAG_NAME, "h3").text
        restaurant_data["sections"] = []
        sections = restaurant.find_elements(By.TAG_NAME, "ns-menu-station")
        if not sections:
            foods = restaurant.find_elements(By.TAG_NAME, "a")
            restaurant_data["foods"] = [food.text for food in foods]
        for section in sections:
            section_data = {}
            section_data["section_title"] = section.find_element(By.TAG_NAME, "h3").text
            foods = section.find_elements(By.TAG_NAME, "a")
            section_data["foods"] = [food.text for food in foods]
            restaurant_data["sections"].append(section_data)
        data.append(restaurant_data)
    return data

from datetime import datetime
from urllib.parse import urljoin
def scrape_restaurant(hall):
    date = datetime.today().strftime('%Y-%m-%d')
    data = {}
    data["hall_name"] = hall
    for meal in ["breakfast", "lunch", "dinner"]:
        url = "/".join([url_prefix, hall, meal, date])
        meal_data = scrape_menu(url)
        if meal_data: data[meal] = meal_data
    return data

import json
hall_names = ["gordon-avenue-market", "rhetas-market", "lowell-market", "lizs-market", "carsons-market", "four-lakes-market"]
def scrape_all_restaurants():
    date = datetime.today().strftime('%Y-%m-%d')
    data = []
    for hall in hall_names:
        data.append(scrape_restaurant(hall))
    with open("data/" + date, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)