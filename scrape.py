import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = "https://wisc-housingdining.nutrislice.com/menu/gordon-avenue-market/lunch/2023-09-25"

def scrape_menu(url):
    browser.get(url)
    browser.implicitly_wait(3)
    btn = browser.find_element(By.XPATH,'//button[text()="View Menus"]')
    btn.click()
    browser.implicitly_wait(3)

    menu = browser.find_element(By.CLASS_NAME, "menu-container")
    restaurants = menu.find_elements(By.TAG_NAME, "ns-menu-section")

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
        

