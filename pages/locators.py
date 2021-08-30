from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, '[class="container-fluid page"] .page_inner')
    AUTH_BUT = (By.CSS_SELECTOR, '[name = "login_submit"]')
    REG_BUT = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BIN_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    STAFF_NAME = (By.CSS_SELECTOR, '.product_main h1')
    STAFF_NAME_AFTER_ADD = (By.CSS_SELECTOR, '.alert:nth-child(1) .alertinner strong')
    SUCCESS_MESSAGE = [By.CSS_SELECTOR, '#messages .alert:nth-child(1)']
    DISAPPEARED_MESSAGE = (By.CSS_SELECTOR, '#messages .alert:nth-child(1)')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
