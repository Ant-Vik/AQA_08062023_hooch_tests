from pages.start_page import StartPage
from constants.start_page_constants import StartPageConstantsLocators
from constants.expected_results.start_page_ex_res import StartPageER


start_page = StartPage()

"""tests"""


def test_compare_url(logger_fixture, driver_google):
    assert StartPageConstantsLocators.URL == StartPageER.ex_res_url
    log = logger_fixture
    log.info('test_compare_url был запущен')


def test_get_h1(logger_fixture, driver_get_h1):
    assert driver_get_h1 == StartPageER.ex_res_get_h1
    log = logger_fixture
    log.info('test_get_h1 был запущен')


def test_tag_a_href(logger_fixture):
    assert StartPageConstantsLocators.LOGO_URL == StartPageER.ex_res_a_href_logo
    log = logger_fixture
    log.info('test_tag_a_href был запущен')


def test_menu(logger_fixture):
    assert start_page.driver_header_menu_first_item(StartPageConstantsLocators.URL) == StartPageER.ex_res_first_menu_item
    log = logger_fixture
    log.info('test_menu был запущен')


def test_search_second_demo(logger_fixture):
    assert start_page.driver_search_second_demo(StartPageConstantsLocators.URL) == StartPageER.ex_res_second_demo
    log = logger_fixture
    log.info('test_search_second_demo был запущен')


def test_search_list(logger_fixture):
    assert start_page.driver_search_list(StartPageConstantsLocators.URL) == StartPageER.ex_res_first_list_item
    log = logger_fixture
    log.info('test_search_list был запущен')


def test_banner_src(logger_fixture):
    assert start_page.driver_banner(StartPageConstantsLocators.URL) == StartPageER.ex_res_banner_src
    log = logger_fixture
    log.info('test_banner_src был запущен')