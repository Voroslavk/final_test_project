from selenium.webdriver.common.by import By


class MainPageLocators:
    BIN_BUTTON = (By.CSS_SELECTOR, '.btn-group .btn-default:nth-child(1)')
    TEXT_OF_EMPTY_BIN = (By.CSS_SELECTOR, '#content_inner p')
    COMPLETE_PURCHASE = (By.CSS_SELECTOR, '.col-sm-offset-8 a')


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


class BinPageLocators:
    GO_TO_HOME_FROM_BIN = (By.CSS_SELECTOR, ".breadcrumb li a")
    CONTINUE_SHOPPING_FROM_BIN = (By.CSS_SELECTOR, "#content_inner p a")
    WE_INSIDE_BASKET = (By.CSS_SELECTOR, ".page-header h1")
