from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import BasePage

class Home_page(BasePage):
    FORGOT_PASSWORD_LINK = (By.XPATH, '//a[@href = "/forgot_password"]')
    FORM_AUTH_LINK = (By.XPATH, '//a[@href = "/login"]')
    INPUTS_LINK = (By.XPATH, '//a[@href = "/inputs"]')
    KEY_PRESSES_LINK = (By.XPATH, '//a[@href = "/key_presses"]')

    def navigate_to_web_page(self):
        self.driver.get('https://the-internet.herokuapp.com/')

    def click_forgot_password(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()

    def click_form_auth(self):
        self.driver.find_element(*self.FORM_AUTH_LINK).click()

    def click_inputs(self):
        self.driver.find_element(*self.INPUTS_LINK).click()

    def click_key_presses(self):
        self.driver.find_element(*self.KEY_PRESSES_LINK).click()
