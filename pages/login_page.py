from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def login_form_exist(self):
        pass

    def authorization_exist_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        password_input.send_keys(password)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

