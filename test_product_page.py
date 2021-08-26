import time
import pytest
from .pages.product_page import BinPage
from .pages.base_page import BasePage


@pytest.mark.parametrize('link', ["?promo=offer0", pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer9"])
def test_adding_of_staff_in_bin(browser, link):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link}'
    page = BinPage(browser, link)
    page.open()
    page.add_to_bin()
    page.solve_quiz_and_get_code()
    page.check_purchase_name()