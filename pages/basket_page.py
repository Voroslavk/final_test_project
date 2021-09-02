from .base_page import BasePage
from .locators import BinPageLocators


class BasketPage(BasePage):
    def go_to_home_from_basket(self):
        self.browser.find_element(*BinPageLocators.GO_TO_HOME_FROM_BIN).click()

    def go_to_continue_shipping_from_bin(self):
        self.browser.find_element(*BinPageLocators.CONTINUE_SHOPPING_FROM_BIN).click()

    def we_inside_basket_check(self):
        assert self.is_element_present(*BinPageLocators.WE_INSIDE_BASKET)

