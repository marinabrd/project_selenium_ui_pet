from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .base_page import BasePage

# обьявляем дочерний класс

# Функция перехода на страницу логина


class MainPage(BasePage):
    def go_to_login(self):
        # находим элемент CSS SELECTOR "JS Path", заменяем его ссылкой на файл, * это пара значений
        # наименование селектора и сам селектор
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)

        login_link.click()

