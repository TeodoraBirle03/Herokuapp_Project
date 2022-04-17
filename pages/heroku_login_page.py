from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import BasePage

class Login_page(BasePage):
    USERNAME_INPUT = (By.XPATH,'//input[@id="username"]')
    PASS_INPUT = (By.XPATH, '//input[@id="password"]')
    LOGIN_BTN = (By.XPATH, '//button/i[text() =" Login"]')
    # ELEMENTAL_SELENIUM_LINK = (By.XPATH, '//a[@href="http://elementalselenium.com/"]')

    def navigate_to_login_page(self):
        self.driver.get('https://the-internet.herokuapp.com/login')

    def fill_username(self):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys('tomsmith')

    def fill_password(self):
        self.driver.find_element(*self.PASS_INPUT).send_keys('SuperSecretPassword!')

    def click_login_btn(self):
        self.driver.find_element(*self.LOGIN_BTN).click()