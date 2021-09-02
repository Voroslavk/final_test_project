from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def there_is_empty_bin(self):
        assert self.is_not_element_present(*MainPageLocators.COMPLETE_PURCHASE), "There is stuff"

    def there_is_text_about_empty_bin(self):
        assert self.is_element_present(*MainPageLocators.TEXT_OF_EMPTY_BIN), "There is text about empty bin"
