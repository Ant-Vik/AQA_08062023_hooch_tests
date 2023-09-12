from pages.start_page import StartPage
from constants.start_page_constants import StartPageConstantsLocators
from constants.expected_results.start_page_ex_res import StartPageER


start_page = StartPage()

"""tests"""


def test_compare_url():
    assert start_page.driver_current_url(StartPageConstantsLocators.URL) == StartPageER.ex_res_url


def test_get_h1():
    assert start_page.driver_get_h1(StartPageConstantsLocators.URL) == StartPageER.ex_res_get_h1


def test_tag_a_href(logger_fixture, driver_google):
    assert start_page.driver_get_tag(StartPageConstantsLocators.URL) == StartPageER.ex_res_a_href_logo
    log = logger_fixture
    log.info('test_tag_a_href был запущен')

def test_menu():
    assert start_page.driver_header_menu_first_item(StartPageConstantsLocators.URL) == StartPageER.ex_res_first_menu_item


def test_search_second_demo():
    assert start_page.driver_search_second_demo(StartPageConstantsLocators.URL) == StartPageER.ex_res_second_demo


def test_search_list():
    assert start_page.driver_search_list(StartPageConstantsLocators.URL) == StartPageER.ex_res_first_list_item


def test_banner_src():
    assert start_page.driver_banner(StartPageConstantsLocators.URL) == StartPageER.ex_res_banner_src
