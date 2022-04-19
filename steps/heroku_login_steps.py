from behave import *

# @when('heroku_home: I click on the Form Authentication link')
# def step_impl(context):
#     context.heroku_home_page.click_form_auth()

@given('heroku_login_page: I am a user on the https://the-internet.herokuapp.com/login page')
def step_impl(context):
    context.heroku_login_page.navigate_to_login_page()

@when('heroku_login_page: I fill {username} in the username field')
def step_impl(context, username):
    context.heroku_login_page.fill_username(username)

@when('heroku_login_page: I fill {password} in the password field')
def step_impl(context, password):
    context.heroku_login_page.fill_password(password)

@when('heroku_login_page: I click on the Login button')
def step_impl(context):
    context.heroku_login_page.click_login_btn()

@then('heroku_login_page: I see the error message displayed')
def step_impl(context):
    context.heroku_login_page.see_error_message()

@when('heroku_login_page: I click the X on the error message banner')
def step_impl(context):
    context.heroku_login_page.click_error_message()

@then('heroku_login_page: I not see the error message displayed anymore')
def step_impl(context):
    context.heroku_login_page.see_error_message()
