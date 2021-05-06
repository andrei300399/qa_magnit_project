from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_email_form_ms(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_EMAIL), "Login email input form is not presented"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM_BUTTON_MS), "Login button microsoft is not presented"

    def should_be_password_form_ms(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM_PASSWORD), "Login password input form is not presented"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM_BUTTON_MS), "Login button microsoft is not presented"

    def authorization_exist_user(self, email, password):
        self.should_be_login_form()
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        self.should_be_email_form_ms()
        email_input = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_EMAIL)
        email_input.send_keys(email)
        button_continue1 = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_BUTTON_MS)
        button_continue1.click()
        password_input = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_PASSWORD)
        password_input.send_keys(password)
        time.sleep(5)
        button_continue2 = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_BUTTON_MS)
        button_continue2.click()
        button_continue3 = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON_MS_CONTINUE)
        button_continue3.click()
        button_continue4 = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON_NOT_EXIT)
        button_continue4.click()
        button_continue6 = self.browser.find_element(*LoginPageLocators.LOGIN_ERROR_TO_HOME)
        button_continue6.click()
        button_continue5 = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON_APP_CONTINUE)
        button_continue5.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_NAME_IN_LK)
