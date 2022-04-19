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
    ERROR_LOGIN = (By.XPATH, '//div[@class="flash error"]')
    X_BUTTON = (By.XPATH, '//a[@class="close"]')
    # ELEMENTAL_SELENIUM_LINK = (By.XPATH, '//a[@href="http://elementalselenium.com/"]')

    def navigate_to_login_page(self):
        self.driver.get('https://the-internet.herokuapp.com/login')

    def fill_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def fill_password(self, password):
        self.driver.find_element(*self.PASS_INPUT).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def see_error_message(self):
        actual = self.driver.find_element(*self.ERROR_LOGIN).text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'The error message is not displayed!')

    def click_error_message(self):
        self.driver.find_element(*self.X_BUTTON).click()

    def not_see_error_message(self):
        try:
            self.driver.find_element(*self.ERROR_LOGIN).text
            raise Exception("The error message is still displayed!")
        except NoSuchElementException:
            pass