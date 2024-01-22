from behave import *

@when('Careers page: I click  on "{alege_oras}" from Alege_oras box')
def step_impl(context, alege_oras):
    context.careers_page.choose_city_from_city_box(alege_oras)


@when('Careers page: I click on "{alege_magazin}" from Alege_magazin box')
def step_impl(context, alege_magazin):
    context.careers_page.choose_store_from_city_box(alege_magazin)

@when('Careers page: I click on Looking for a job button')
def step_impl(context):
    context.careers_page.click_search_job_button()


@then('Careers page: I have at least "{no_of_results}" results returned')
def step_impl(context, no_of_results):
    context.careers_page.check_job_search_results(no_of_results)









