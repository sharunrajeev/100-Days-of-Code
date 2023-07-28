from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# no_of_articles = driver.find_element(By.XPATH, '//*[@id="searchform"]/div/div/div[1]/input').text
# print(no_of_articles)

search_bar = driver.find_element(By.NAME, 'search')
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)

# driver.quit()
