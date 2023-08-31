from constants.start_page_constants_locators import StartPageConstantsLocators
from constants.demo_page_constants import DemoConstants
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://vulkanbet.club/'


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


    def driver_get_h1(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(2)
        driver.get(url)
        sleep(2)
        h2 = driver.find_element(By.XPATH, value=StartPageConstantsLocators.SEARCH_H1_IN_PAGE)
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

    def driver_header_menu_first_item(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(url)
        menu_item = driver.find_element(By.XPATH, value=StartPageConstantsLocators.HEADER_MENU_FIRST_ITEM)
        menu_item_text = menu_item.text
        return menu_item_text


    def driver_search_second_demo(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(url)
        find_second_demo = driver.find_elements(By.XPATH, value=DemoConstants.ALL_DEMOS_IN_PAGE)
        second_demo = find_second_demo[1]
        find_button_demo = second_demo.find_element(By.XPATH, value=DemoConstants.SLOT_BUTTON)
        find_button_link_demo = find_button_demo.find_elements(By.TAG_NAME, 'a')
        second_demo_button = find_button_link_demo[1]
        href_button_link_demo = second_demo_button.get_attribute('href')
        return href_button_link_demo

    def driver_search_list(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(url)
        find_ul_list = driver.find_elements(By.CSS_SELECTOR, value='ul')
        second_ul_list = find_ul_list[2]
        find_li_in_ul_list = second_ul_list.find_elements(By.TAG_NAME, value='li')
        list_li_text = find_li_in_ul_list[0].text
        return list_li_text

    def driver_banner(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(url)
        header_banner = driver.find_element(By.XPATH, value=StartPageConstantsLocators.HEADER_BANNER)
        header_banner_picture = header_banner.find_element(By.TAG_NAME, 'picture')
        header_banner_img = header_banner_picture.find_element(By.TAG_NAME, 'img')
        header_banner_img_attribute = header_banner_img.get_attribute('src')
        return header_banner_img_attribute


conf = Configure()


def test_compare_url():
    assert conf.driver_current_url(url) == "https://vulkanbet.club/"


def test_get_h1():
    assert conf.driver_get_h1(url) == "VulkanBet – Sportwetten und Casino Spiele"


def test_tag_a_href():
    assert conf.driver_get_tag(url) == "https://vulkanbet.club/go/logo/"

def test_menu():
    assert conf.driver_header_menu_first_item(url) == "ONLINE CASINO"

def test_search_second_demo():
    assert conf.driver_search_second_demo(url) == "https://vulkanbet.club/ultra-hot-deluxe/"

def test_search_list():
    assert conf.driver_search_list(url) == "Sweet Life;"

def test_banner_src():
    assert conf.driver_banner(url) == "https://vulkanbet.club/wp-content/uploads/sites/10004/heroimg-1.jpg"