from selenium import webdriver
from selenium.webdriver.common.by import By

username = "USERNAME"
password = "PASSWORD"
phone = "PHONE"

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")


def sign_in():
    driver.find_element(By.LINK_TEXT, "Sign in").click()
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
    not_now = driver.find_element(By.LINK_TEXT, "Not now")
    not_now.click()


def apply_job():
    apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
    apply_button.click()
    phone_input = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
    if phone_input.text == "":
        phone_input.send_keys(phone)
    # Submit
    driver.find_element(By.CSS_SELECTOR, "footer button").click()

