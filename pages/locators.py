from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_btn")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password_input")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#email_input")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class AdminPageLocators:
    pass


class AccountPageLocators:
    pass
