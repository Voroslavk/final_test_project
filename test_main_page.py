import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    time.sleep(5)
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_the_bin()
    page.there_is_empty_bin()
    page.there_is_text_about_empty_bin()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_the_bin()
    page.there_is_empty_bin()
    page.there_is_text_about_empty_bin()


def test_for_empty_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/basket/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_home_from_basket()
    page.go_to_the_bin()
    page.go_to_continue_shipping_from_bin()


def test_there_is_no_message_for_bin(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/basket/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
