from behave import *

@when('Careers page: I click  on "<alege oras>" from "Alege oras" box')
def step_impl(context, alege_oras):
    context.careers_page.choose_search_value(alege_oras)


@when('Careers page: I click on "<alege magazin>" from "Alege magazin" box')
def step_impl(context, alege_magazin):
    context.careers_page.choose_search_value(alege_magazin)

@when('Careers page: I click on Looking for a job button')
def step_impl(context):
    context.careers_page.click_on_looking_for_a_job_button()


@then('Careers page: I have at least "<no_of_results>" results returned')
def step_impl(context, no_of_results):
    context.careers_page.check_search_results(no_of_results)









