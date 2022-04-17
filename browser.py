from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Browser():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()

    def close(self):
        self.driver.close()