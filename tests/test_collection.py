from tests import test_webdriver_methods
from test_webdriver_methods import Configure


def test_compare_url():
    assert Configure.driver_current_url(test_webdriver_methods.url) == "https://www.slotozilla.com/"