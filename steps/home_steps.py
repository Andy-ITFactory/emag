from behave import *


@given('home: I am a user on emag.ro Home page')
def step_impl(context):
    context.home_page.navigate_to_home_page()
    context.home_page.click_accept_cookies_btn()
    context.home_page.click_intra_in_cont_close_btn()


@when('home: I click on contul meu')
def step_impl(context):
    context.home_page.click_contul_meu_btn()


@when('home: I search after "{query}"')
def step_impl(context, query):
    context.home_page.search_after(query)


@then('home: I verify login message "{message}"')
def step_impl(context, message):
    context.home_page.verify_login_message(message)


@then('home: I verify home page url')
def step_impl(context):
    context.home_page.verify_url_message()

