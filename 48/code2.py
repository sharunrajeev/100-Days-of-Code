from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.python.org/")

dates = driver.find_elements(By.CSS_SELECTOR, "#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > time")
names = driver.find_elements(By.CSS_SELECTOR, "#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > a")
events = {}

for i in range(len(dates)):
    events[i] = {
        "time": dates[i].text,
        "name": names[i].text
    }

print(events)
