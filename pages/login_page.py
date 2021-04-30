from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def authorization_exist_user(self, email, password):
        self.should_be_login_form()
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    # def authorization_empty_form(self):
    #     self.authorization_exist_user(email="", password="")
    #     assert self.is_element_present(*LoginPageLocators.LOGIN_ALERT_EMPTY), "Alert about empty form is not presented"
    #
    # def authorization_not_exist_user(self, email, password):
    #     self.authorization_exist_user(email=email, password=password)
    #     assert self.is_element_present(*LoginPageLocators.LOGIN_ALERT_NOT_EXIST_USER), "Alert about not exsist user is not presented"
