# Cookie clicker game

from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, '#cookie')
item_ids = [item.get_attribute("id") for item in driver.find_elements(By.CSS_SELECTOR, "#store div")]
item_ids.pop()
print(item_ids)

five_secs = time() + 5
five_min = time() + 300
while True:
    cookie.click()

    if time() > five_secs:
        # get_price_of_items
        cookie_upgrades = {}
        for ids in item_ids:
            if ids == "buyAlchemy lab" or ids == "buyTime machine":
                new_ids = ids.replace(" ", "\ ")
                cookie_upgrades[ids] = driver.find_element(By.CSS_SELECTOR, f"#{new_ids} > b").text.split(' ')[
                    3].replace(
                    ",", "")
            else:
                cookie_upgrades[ids] = driver.find_element(By.CSS_SELECTOR, f"#{ids} b").text.split(' ')[2].replace(",", "")

        # get number of cookies
        cookie_count = driver.find_element(By.CSS_SELECTOR, '#money').text

        # get affordable item
        affordable_item = {}
        for item_id, cost in cookie_upgrades.items():
            if int(cost) < int(cookie_count):
                affordable_item[cost] = item_id

        # Select most expensive item
        highest_affordable_item = max(affordable_item)
        print(highest_affordable_item)
        driver.find_element(By.ID, affordable_item[highest_affordable_item]).click()

        five_secs += 5

    if time() > five_min:
        cps = driver.find_element(By.ID, "cps")
        print(f"Cookies/second : {cps}")
        break
