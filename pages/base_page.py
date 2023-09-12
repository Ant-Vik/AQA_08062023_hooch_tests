from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self):
        self.options = ChromeOptions()
        self.options.headless = False
        self.options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        # self.driver.implicitly_wait(20)
        self.wait = WebDriverWait(self.driver, 10)

