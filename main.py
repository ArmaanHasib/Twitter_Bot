import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

PROMISED_DOWN = 30
PROMISED_UP = 15
CHROME_DRIVER_PATH = 'C:\\Users\\sunny\\Downloads\\chromedriver_win32\\chromedriver.exe'

TWITTER_EMAIL = os.getenv('email')
TWITTER_PASSWORD = os.getenv('password')

class InternetSpeedTwitterBot:
    def __init__(self):
        # self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.speedtest.net/')
        time.sleep(2)
        accept_button = driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        accept_button.click()
        time.sleep(2)
        go_button = driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(20)
        down_speed_value = driver.find_element(By.XPATH,
                                               '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        time.sleep(20)
        up_speed_value = driver.find_element(By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(f"Down: {down_speed_value}")
        print(f"Up: {up_speed_value}")
        time.sleep(5)
        driver.quit()




    def tweet_at_provider(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.x.com/')
        time.sleep(2)
        cancel_button = driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div[2]/div/div/div/button')
        cancel_button.click()
        time.sleep(2)
        google_login = driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[2]/span[1]')
        google_login.click()


speed_bot = InternetSpeedTwitterBot()
#speed_bot.get_internet_speed()
speed_bot.tweet_at_provider()


