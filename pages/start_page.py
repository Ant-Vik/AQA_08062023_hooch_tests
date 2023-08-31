from constants.start_page_constants_locators import StartPageConstantsLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class StartPage(BasePage):
    def __int__(self):
        super.__init__()



    def driver_current_url(self, url):
        self.driver.get(url)  # Открываем сайт по урлу
        return self.driver.current_url

    def driver_get_h1(self, url):
        self.driver.get(url)
        h1 = self.driver.find_element(By.XPATH, value=StartPageConstantsLocators.SEARCH_H1_IN_PAGE)  # Находим h1 элемент
        h1_text = h1.text  # Превращаем найденный элемент в текст
        return h1_text

    def driver_get_tag(self, url):
        self.driver.get(url)
        tag_a = self.driver.find_element(By.TAG_NAME, value='a')  # Находим тег а на странице
        href_value = tag_a.get_attribute('href')  # Находим значение атрибута href
        return href_value