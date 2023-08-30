from constants.start_page_constants_locators import StartPageConstantsLocators
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.slotozilla.com/'


class Configure:


    def driver_current_url(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(1)
        driver.get(url)
        return driver.current_url


    def driver_get_text(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(2)
        driver.get(url)
        sleep(2)
        h2 = driver.find_element(By.XPATH, value=StartPageConstantsLocators.SEARCH_H2_IN_PAGE)
        h2_text = h2.text
        sleep(2)
        return h2_text


    def driver_get_tag(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(2)
        driver.get(url)
        sleep(2)
        tag_a = driver.find_element(By.TAG_NAME, value='a')
        href_value = tag_a.get_attribute('href')
        return href_value


    def driver_search(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(2)
        driver.get(url)
        search_button = driver.find_element(By.XPATH, value=".//div[@class='header-search-hide']")
        sleep(2)
        search_button.click()
        sleep(2)
        input_field = driver.find_element(By.XPATH, value=".//input[@id='s']")
        input_field.click()
        sleep(2)
        input_field.clear()
        input_field.send_keys("testttt")
        input_field.send_keys(Keys.ENTER)
        nothing_found_message = driver.find_element(By.XPATH, value=".//div[@class='nothing-found']")
        nothing_found_message_text = nothing_found_message.text
        return nothing_found_message_text

    def driver_switch(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(2)
        driver.get(url)
        ref_button = driver.find_element(By.XPATH, value='test')


conf = Configure()


# def test_compare_url():
#     assert conf.driver_current_url(url) == "https://www.slotozilla.com/"


def test_hq_text():
    assert conf.driver_get_text(url) == "How We Select the Best Online Casinos"


def test_href():
    assert conf.driver_get_tag(url) == "https://www.slotozilla.com/au/"


def test_search():
    assert conf.driver_search(url) == ("It seems we can’t find what you’re looking for. Perhaps you should try again with a "
                                  "different search term.")