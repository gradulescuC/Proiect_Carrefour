from behave import *


@when('My basket page: The user clicks on remove product from the cart button')
def step_impl(context):
    context.basket_page.click_on_remove_button()


@then('My basket page: The user received a message that the basket is empty')
def step_impl(context):
    context.basket_page.the_product_is_removed()


@then('My Basket: The product should be found in the shopping cart')
def step_impl(context):
    context.basket_page.product_should_be_found_in_cart()