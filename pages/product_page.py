from base_page import BasePage
from locators import ProductPageLocators


class BinPage(BasePage):
    def add_to_bin(self):
        addbutton = self.browser.find_element(*ProductPageLocators.ADD_TO_BIN_BUTTON)
        addbutton.click()

    def check_purchase_name(self):
        staff_name_do = self.browser.find_element(*ProductPageLocators.STAFF_NAME)
        staff_name_text = staff_name_do.text
        staff_name_aft = self.browser.find_element(*ProductPageLocators.STAFF_NAME_AFTER_ADD)
        staff_name_two = staff_name_aft.text

        assert staff_name_text == staff_name_two, 'Should be the same'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.DISAPPEARED_MESSAGE), \
            "Success message is presented, but should not be"
