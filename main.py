from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

PROMISED_DOWN = 30.00
PROMISED_UP = 15.00
CHROME_DRIVER_PATH = 'C:\\Users\\sunny\\Downloads\\chromedriver_win32\\chromedriver.exe'

TWITTER_EMAIL = os.getenv('email')
TWITTER_PASSWORD = os.getenv('password')


class InternetSpeedTwitterBot:
    def __init__(self):
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
        # down_speed_value = driver.find_element(By.XPATH,
        #                                        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        down_speed_value = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'))).text
        time.sleep(20)
        up_speed_value = driver.find_element(By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(f"Down: {down_speed_value}")
        print(f"Up: {up_speed_value}")
        self.down = float(down_speed_value)
        self.up = float(up_speed_value)
        time.sleep(5)
        driver.quit()




    def tweet_at_provider(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://twitter.com/i/flow/login')

        email_id = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
        email_id.send_keys(TWITTER_EMAIL)
        email_id.send_keys(Keys.ENTER)

        password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(10)

        tweet = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Hey Internet Provider!\n"
                        f"I am paying for the Rs.399 plan where I am promised a download speed of 30Mbps but I am only getting {self.down}Mbps."
                        f"Need this to be resolved ASAP! \n\n#jio #jiofiber")
        post = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span')
        post.click()
        time.sleep(10)

        driver.quit()


speed_bot = InternetSpeedTwitterBot()
speed_bot.get_internet_speed()
if speed_bot.down < PROMISED_DOWN:
    speed_bot.tweet_at_provider()

