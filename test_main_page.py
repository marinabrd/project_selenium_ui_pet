from .pages.main_page import MainPage

# Пишем тест, слово test должно присутствовать


def test_to_gologin_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login()
    browser.save_screenshot('result8.png')
# Terminal: pytest test_main_page.py
# Пример использования LoginPage в тесте
from pages.login_page import LoginPage

#ChatGPT
login_page = LoginPage(browser, url)
login_page.go_to_login()
login_page.enter_password("your_password")
login_page.click_login_button()
