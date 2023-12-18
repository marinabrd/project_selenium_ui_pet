import time

from .pages.login_page import LoginPage


def test_go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
# Открываем страницу логина
    page = LoginPage(browser, link)
    page.open()
# Вводим логин
    page.go_to_login()
# Вводим пароль и нажимаем кнопку входа
    page.enter_password()

# Не успевает залогиниться, добавляем задержку
    time.sleep(10)

    page.click_login_button()

    browser.save_screenshot('result11.png')

#Terminal: "pytest test_login_page.py"
#Terminal alternative: "pytest -vtests/ test_login_page.py
# pip freeze>requirements.txt (?)









#import pytest
#from selenium import webdriver
#from selenium.webdriver.common.by import By


#link = "http://34.141.58.52:8080/#/login"


#@pytest.fixture(autouse=True)
#def browser():
 #   browser = webdriver.Chrome()
  #  yield browser
   # browser.quit()


#def input_login(browser):
 #   input1 = browser.find_element(By.ID, "login")
  #  input1.send_keys("mox@gmx.org")


#class TestLogin:

 #   def test_input_login(self, browser):
  #      browser.get(link)
   #     input_login(browser)

    #def test_input_password(self, browser):
     #   browser.get(link)
      #  input2 = browser.find_element(By.CSS_SELECTOR, "#password > input")
       # input2.send_keys("RoTderGott7096")

    #def test_submit_button(self, browser):
     #   browser.get(link)
      #  button = browser.find_element(By.CLASS_NAME, "p-button-label")
       # button.submit()

        #browser.save_screenshot('result_7.png')