from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, '[class="container-fluid page"] .page_inner')
    AUTH_BUT = (By.CSS_SELECTOR, '[name = "login_submit"]')
    REG_BUT = (By.CSS_SELECTOR, '[name="registration_submit"]')
