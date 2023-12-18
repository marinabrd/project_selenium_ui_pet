from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('mox@gmx.org')

    def enter_password(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys('RoTderGott7096')

    def click_login_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_button.submit()
        #login_button.click() #!!!! вызывает ошибку, не подходит для submit BTN
