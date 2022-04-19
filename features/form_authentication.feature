Feature: Herokuapp form_authentication tests

  Background:
    Given heroku_home_page: I am on the https://the-internet.herokuapp.com/ page

    @form_auth_flow1
    Scenario: The form_authentication flow with correct username and password
      When heroku_home_page: I click on the Form Authentication link
      When heroku_login_page: I fill tomsmith in the username field
      When heroku_login_page: I fill SuperSecretPassword! in the password field
      When heroku_login_page: I click on the Login button
      When heroku_secure_page: I see the login success message
      When heroku_secure_page: I click on the Logout button
      Then heroku_secure_page: I verify that I am on the heroku_login_page

    @form_auth_flow2
    Scenario: The form_authentication flow with invalid username and password
      When heroku_home_page: I click on the Form Authentication link
      When heroku_login_page: I fill user in the username field
      When heroku_login_page: I fill Password in the password field
      When heroku_login_page: I click on the Login button
      Then heroku_login_page: I see the error message displayed
      When heroku_login_page: I click the X on the error message banner
      Then heroku_login_page: I not see the error message displayed anymore

