from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

# in aceasta pagina punem toate metodele care sunt utile in orice pagina din proiect
# si nu sunt specifice neaparat unei singure pagini
# apoi paginile vor mosteni aceasta pagina => ca sa nu scrie de n ori wait_for_elem and other helper methods
class BasePage(Browser, unittest.TestCase):

    def wait_for_elem(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))