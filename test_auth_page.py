from .pages.login_page import LoginPage


def test_user_can_auth_or_reg(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url(), 'Что-то тут'
    page.should_be_login_form(), 'Xnjefk'
    page.should_be_register_form(), 'Chto-to tyt'
