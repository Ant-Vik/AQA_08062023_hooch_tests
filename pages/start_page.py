from constants.start_page_constants import StartPageConstantsLocators
from pages.base_page import BasePage
from constants.demo_page_constants import DemoConstants
from selenium.webdriver.common.by import By


class StartPage(BasePage):
    def __init__(self):
        super().__init__()

    def driver_current_url(self, url):
        # Открываем сайт по урлу
        self.driver.get(url)
        return self.driver.current_url

    def driver_get_h1(self, url):
        self.driver.get(url)
        # Находим h1 элемент
        h1 = self.driver.find_element(By.XPATH, value=StartPageConstantsLocators.SEARCH_H1_IN_PAGE)
        # Превращаем найденный элемент в текст
        h1_text = h1.text
        return h1_text

    def driver_get_tag(self, url):
        self.driver.get(url)
        # Находим тег, а на странице
        tag_a = self.driver.find_element(By.TAG_NAME, value='a')
        # Находим значение атрибута href
        href_value = tag_a.get_attribute('href')
        return href_value

    def driver_header_menu_first_item(self, url):
        self.driver.get(url)
        # Находим первый пункт меню на странице
        menu_item = self.driver.find_element(By.XPATH, value=StartPageConstantsLocators.HEADER_MENU_FIRST_ITEM)
        menu_item_text = menu_item.text
        return menu_item_text

    def driver_search_second_demo(self, url):
        self.driver.get(url)
        # Находим все демки на странице
        find_second_demo = self.driver.find_elements(By.XPATH, value=DemoConstants.ALL_DEMOS_IN_PAGE)
        # Выбираем из списка демок второй по порядку элемент
        second_demo = find_second_demo[1]
        # Находим кнопки второй демки на странице
        find_button_demo = second_demo.find_element(By.XPATH, value=DemoConstants.SLOT_BUTTON)
        # Находим тег в котором указанны ссылки на кнопки
        find_button_link_demo = find_button_demo.find_elements(By.TAG_NAME, 'a')
        # Выбираем из двух ссылок ссылку на демку
        second_demo_button = find_button_link_demo[1]
        # Смотрим искомую ссылку
        href_button_link_demo = second_demo_button.get_attribute('href')
        return href_button_link_demo

    def driver_search_list(self, url):
        self.driver.get(url)
        # Ищем таблицу на странице
        find_ul_list = self.driver.find_elements(By.CSS_SELECTOR, value='ul')
        # Выбираем нужную нам таблицу из списка
        second_ul_list = find_ul_list[2]
        # Находим в таблице элементы li
        find_li_in_ul_list = second_ul_list.find_elements(By.TAG_NAME, value='li')
        # Выбираем первый элемент li из списка элементов
        list_li_text = find_li_in_ul_list[0].text
        return list_li_text

    def driver_banner(self, url):
        self.driver.get(url)
        # Находим контейнер с баннером
        header_banner = self.driver.find_element(By.XPATH, value=StartPageConstantsLocators.HEADER_BANNER)
        # Находим элемент в котором лежат изображения баннера
        header_banner_picture = header_banner.find_element(By.TAG_NAME, 'picture')
        # Находим тег в котором по атрибуту находится изображение
        header_banner_img = header_banner_picture.find_element(By.TAG_NAME, 'img')
        # Находим изображение баннера
        header_banner_img_attribute = header_banner_img.get_attribute('src')
        return header_banner_img_attribute
