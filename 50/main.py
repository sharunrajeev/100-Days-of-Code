# Creating a tweet machine which would tweet message when you have bad internet speed
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

PROMISED_DOWN = 30
PROMISED_UP = 30
TWITTER_USERNAME = ""
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Edge()
        self.up = 0
        self.down = 0

    def login_to_twitter(self):
        self.driver.get("https://twitter.com/")
        self.driver.find_element(By.XPATH,
                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a').click()
        sleep(10)
        username_input = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                  '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                                  '2]/div/input')
        username_input.send_keys(TWITTER_USERNAME)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                           '2]/div[2]/div/div/div/div[6]').click()
        sleep(10)
        password_input = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                  '2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div['
                                                  '2]/div[1]/input')
        password_input.send_keys(TWITTER_PASSWORD)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                           '2]/div[2]/div[2]/div/div[1]/div/div/div').click()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        sleep(120.0)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                             '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                           '3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        sleep(10)

    def tweet_at_provider(self):
        self.login_to_twitter()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        tweet_input = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                               '2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div['
                                               '2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div['
                                               '1]/div/div/div/div/div/div[2]/div/div/div/div/span')
        tweet_input.send_keys(
            f"My internet speed is too low. I have got only {self.down} and {self.up} which is almost quarter of the plan I have chosen {PROMISED_DOWN} and {PROMISED_UP} #slowinternetspeed #help")
        # Clicks tweet button
        self.driver.find_element(By.XPATH,
                                 '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div['
                                 '2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]').click()
        self.driver.quit()

    def check_speed(self):
        self.get_internet_speed()
        if self.down < (PROMISED_DOWN / 4) or self.up < (PROMISED_UP / 4):
            self.tweet_at_provider()


bot = InternetSpeedTwitterBot()
bot.check_speed()
