from .pages.login_page import LoginPage


def test_user_can_auth_or_reg(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url(), 'login url is valid'
    page.should_be_login_form(), 'login form is here'
    page.should_be_register_form(), 'register form is here'
