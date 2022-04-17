from behave import *

# @when('heroku_home: I click on the Form Authentication link')
# def step_impl(context):
#     context.heroku_home_page.click_form_auth()

@given('heroku_login_page: I am a user on the https://the-internet.herokuapp.com/login page')
def step_impl(context):
    context.heroku_login_page.navigate_to_login_page()

@when('heroku_login_page: I fill tomsmith in the username field')
def step_impl(context):
    context.heroku_login_page.fill_username()

@when('heroku_login_page: I fill SuperSecretPassword! in the password field')
def step_impl(context):
    context.heroku_login_page.fill_password()

@when('heroku_login_page: I click on the Login button')
def step_impl(context):
    context.heroku_login_page.click_login_btn()