from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException

USERNAME = "sharun_rajeev"
PASSWORD = "7rqsZydYgPJFJV"
SIMILAR_ACCOUNT = "chefsteps"


class InstaFollower:
    def __init__(self):
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options=options)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        username_input = self.driver.find_element(By.NAME, 'username')
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        sleep(2)
        followers = self.driver.find_element(By.XPATH,
                                             '//*[@id="mount_0_0_tg"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(2)
        modal = self.driver.find_element(By.XPATH,
                                         '//*[@id="mount_0_0_tg"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div')
        for i in range(10):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR,
                                                '#mount_0_0_tg > div > div > div:nth-child(3) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1) > div > div:nth-child(1) > div > div > div > div:nth-child(3) > div > button')
        for buttons in all_buttons:
            try:
                buttons.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,
                                                         '#mount_0_0_tg > div > div > div:nth-child(3) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1) > div > div:nth-child(1) > div > div > div > div:nth-child(3) > div > button')
                cancel_button.click()

    def run(self):
        self.login()
        self.find_followers()
        self.follow()


bot = InstaFollower()
bot.run()
