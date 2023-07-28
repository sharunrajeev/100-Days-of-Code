from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

driver.find_element(By.XPATH, '/html/body/form/input[1]').send_keys("Neuman")
driver.find_element(By.XPATH, '/html/body/form/input[2]').send_keys("Phil")
driver.find_element(By.XPATH, '/html/body/form/input[3]').send_keys("phil.neuman@mail.com")

driver.find_element(By.XPATH, '/html/body/form/button').click()
