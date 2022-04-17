from pages.heroku_home_page import Home_page
from pages.heroku_login_page import Login_page
from pages.heroku_secure_page import Secure_page
from browser import Browser

def before_all(context):
    context.heroku_home_page = Home_page()
    context.heroku_login_page = Login_page()
    context.heroku_secure_page = Secure_page()
    context.browser = Browser()

def after_all(context):
    context.browser.close()

    # contextul este o cutiuta care contine cate un obiect de tipul fiecarei clase de pagini
    # before all = BDD
    # after all = BDD
    # de fiecare data cand adaugam o pagina noua in proiect o vom adauga in context/un obiect de tipul paginii noi