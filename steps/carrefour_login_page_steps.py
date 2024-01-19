from behave import *


@when('Login page: The user enters "{username}" on the username field')
def step_impl(context,username):
    context.login_page.enter_any_username(username)

@when('Login page: The user enters "{password}" on the password field')
def step_impl(context, password):
    context.login_page.enter_any_password(password)


@when('Login page: The user clicks on login button')
def step_impl(context):
    context.login_page.click_on_login_button()


@then('Login page: User should be logged in')
def step_impl(context):
    context.login_page.login_succesfuly()



