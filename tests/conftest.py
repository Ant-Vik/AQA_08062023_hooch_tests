import pytest
import logging
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from constants.start_page_constants import StartPageConstantsLocators
from pages.base_page import BasePage
from constants.demo_page_constants import DemoConstants
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def logger_fixture():
    # Створіть логер або отримайте існуючий логер
    log = logging.getLogger("Logs: ")
    # Рівень логування (INFO)
    log.setLevel(logging.INFO)
    # Об'єкт для запису в файл
    log_file_handler = logging.FileHandler('test.log', encoding='utf-8')
    # Рівень логування для об'єкта запису в файл
    log_file_handler.setLevel(logging.INFO)
    # Фрматтер для логування в файл
    log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s (%(filename)s:%(lineno)s)')
    # Приєднаэ об'єкт запису в файл до логера
    log_file_handler.setFormatter(log_formatter)
    # Додаємо об'єкт запису в файл до логера
    log.addHandler(log_file_handler)
    # Повертаємо логер з фікстури
    yield log
    # Необхідно очистити логер після використання, щоб уникнути конфліктів
    log.handlers.clear()


@pytest.fixture(scope="function")
def driver_run_brows():
    options = ChromeOptions()
    options.headless = False
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.get(StartPageConstantsLocators.URL)
    return driver


@pytest.fixture()
def driver_get_h1(driver_run_brows):
    h1 = driver_run_brows.find_element(*StartPageConstantsLocators.SEARCH_H1_IN_PAGE)
    h1_text = h1.text
    return h1_text


@pytest.fixture(scope="function")
def driver_get_tag(driver_run_brows):
    wait = WebDriverWait(driver_run_brows, 10)
    tag_a = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'a')))
    href_value = tag_a.get_attribute('href')
    return href_value



