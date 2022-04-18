from behave import *

@given('heroku_secure_page: I am on the https://the-internet.herokuapp.com/secure page')
def step_impl(context):
    context.heroku_secure_page.navigate_to_secure_page()

@when('heroku_secure_page: I see the login success message')
def step_impl(context):
    context.heroku_secure_page.see_message_succes_banner()

@when('heroku_secure_page: I click on the Logout button')
def step_impl(context):
    context.heroku_secure_page.click_Logout()

@then('heroku_secure_page: I verify that I am on the heroku_login_page')
def step_impl(context):
    context.heroku_secure_page.navigate_to_login_page()