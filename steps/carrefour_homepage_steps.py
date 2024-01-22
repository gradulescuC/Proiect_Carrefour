from behave import *

@given('Home page: The user is on https://www.carrefour.ro/')
def step_impl(context):
    context.home_page.navigate_to_homepage()
    context.home_page.accept_cookies()

@when('Home page: The user clicks on account button')
def step_impl(context):
    context.home_page.click_account_button()

@then('Home page: The user should be redirected to login page')
def step_impl(context):
    context.home_page.navigate_to_login_page()

@when('Home page: I search for "{product_name}" from search box')
def step_impl(context, product_name):
    context.home_page.insert_search_value(product_name)

@then('Home Page: I have at least "{results_number}" results returned')
def step_impl(context, results_number):
    context.home_page.check_search_results(results_number)

@when('Home Page: The user type in search box "{product_name}"')
def step_impl(context,product_name):
    context.home_page.type_brad_artificial(product_name)

@when('Home page: The user clicks the search button')
def step_impl(context):
    context.home_page.click_search_button()


@when('Home page: The user clicks on add to basket button')
def step_impl(context):
    context.home_page.click_add_basket_button()


@when("Home page: The user adds the first product to the shopping cart")
def step_impl(context):
    context.home_page.add_product_to_shopping_cart()

@when('Home page: The user clicks on My basket')
def step_impl(context):
    context.home_page.click_my_basket_button()

@when('Home page: I click on careers link')
def step_impl(context):
    context.home_page.click_on_carers_link()








