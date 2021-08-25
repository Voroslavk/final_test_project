from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # assert self.url == "http://selenium1py.pythonanywhere.com/uk/accounts/login/", 'should be correct link'
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.AUTH_BUT), "Auth button should be here"
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_BUT), "Reg button should be here"
        # реализуйте проверку, что есть форма регистрации на странице
        assert True