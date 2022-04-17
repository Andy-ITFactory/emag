from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.cart_page import CartPage
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.login_page = LoginPage()
    context.search_page = SearchPage()
    context.cart_page = CartPage()

def after_all(context):
    context.browser.close()