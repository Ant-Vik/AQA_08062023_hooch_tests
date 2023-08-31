from pages.start_page import StartPage
from constants.start_page_constants_locators import StartPageConstantsLocators
from constants.expected_results.start_page_ex_res import StartPageER

start_page = StartPage()

"""tests"""


def test_compare_url():
    assert start_page.driver_current_url(StartPageConstantsLocators.URL) == StartPageER.ex_res_url


def test_tag_a_href():
    assert start_page.driver_get_tag(StartPageConstantsLocators.URL) == "https://vulkanbet.club/go/logo/"


def test_menu():
    assert start_page.driver_header_menu_first_item(StartPageConstantsLocators.URL) == "ONLINE CASINO"


def test_search_second_demo():
    assert conf.driver_search_second_demo(url) == "https://vulkanbet.club/ultra-hot-deluxe/"


def test_search_list():
    assert conf.driver_search_list(url) == "Sweet Life;"


def test_banner_src():
    assert conf.driver_banner(url) == "https://vulkanbet.club/wp-content/uploads/sites/10004/heroimg-1.jpg"
