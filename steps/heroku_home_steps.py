from behave import *

# given!, when!, and, but, then! - sintaxa gherkin
# given - seteaza situatia initiala
# when - pasii din test
# then - verificarea din test

@given('heroku_home_page: I am on the https://the-internet.herokuapp.com/ page')
def step_impl(context):
    context.heroku_home_page.navigate_to_web_page()

@when('heroku_home_page: I click on the Form Authentication link')
def step_impl(context):
    context.heroku_home_page.click_form_auth()