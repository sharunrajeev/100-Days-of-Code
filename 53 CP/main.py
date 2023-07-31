# Task 1 : Scrap data from Zillow
# Task 2 : Use this data to fill out the form
# Task 3 : Get the data in a spreadsheet

# Imports
from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Constants
ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56825484228516%2C%22east%22%3A-122.29840315771484%2C%22south%22%3A37.69234177970015%2C%22north%22%3A37.858148163315015%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
FORM_LINK = "https://forms.gle/wuEw5r9qo5jJdJNv5"


# Logic
class DataEntryWorker:
    def __init__(self):
        self.address = []
        self.price = []
        self.link = []
        # BeautifulSoup initialisation
        html_doc = get(ZILLOW_LINK, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
            "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8"
        }).content
        self.soup = BeautifulSoup(html_doc, 'lxml')
        # Selenium initialisation
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options)
        self.driver.get(FORM_LINK)

    def get_data_from_zillow(self):
        elements = self.soup.find_all("li",
                                      attrs={
                                          "class": "ListItem-c11n-8-84-3__sc-10e22w8-0 StyledListCardWrapper-srp__sc-wtsrtn-0 iCyebE gTOWtl"})
        for element in elements:
            addr = element.find("address")
            if addr:
                self.address.append(addr.text)
            price_value = element.find("span")
            if price_value:
                self.price.append(price_value.text[:6])
            link_value = element.find("a")
            if link_value:
                link_value = link_value.get("href")
                if link_value[:6] == "https:":
                    self.link.append(link_value)
                else:
                    self.link.append(f"https://www.zillow.com/{link_value}")

    def update_form(self):
        sleep(2)
        length = max(len(self.address), len(self.link), len(self.price))
        for item in range(length):
            address_input = self.driver.find_element(By.XPATH,
                                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input = self.driver.find_element(By.XPATH,
                                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input = self.driver.find_element(By.XPATH,
                                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input.send_keys(self.address[item])
            price_input.send_keys(self.price[item])
            link_input.send_keys(self.link[item])
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
            sleep(1)
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
            sleep(2)


worker = DataEntryWorker()
worker.get_data_from_zillow()
worker.update_form()
