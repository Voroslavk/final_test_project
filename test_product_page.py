import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_bin()
    page.should_not_be_success_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/'
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user()
        page.click_button()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_bin()
        page.check_purchase_name()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_the_bin()
    page.there_is_empty_bin()
    page.there_is_text_about_empty_bin()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_bin()
    page.message_is_disappeared()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/'
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.parametrize('link',
                         ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4",
                          "?promo=offer5", "?promo=offer6",
                          pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                          "?promo=offer8", "?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link}'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_bin()
    page.solve_quiz_and_get_code()
    page.check_purchase_name()
