import pytest
from pages.product_page import ProductPage
from pages.base_page import BasePage


@pytest.mark.parametrize('link', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4",
                                  "?promo=offer5", "?promo=offer6",
                                  pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                  "?promo=offer8", "?promo=offer9"])
def test_adding_of_staff_in_bin(browser, link):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link}'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_bin()
    page.solve_quiz_and_get_code()
    page.check_purchase_name()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_bin()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_bin()
    page.message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/'
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()


