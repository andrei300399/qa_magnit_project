from .base_page import BasePage
from .login_page import LoginPage
from .locators import AccountPageLocators


class AccountPage(BasePage):
    def should_be_account_form(self):
        assert self.is_element_present(*AccountPageLocators.ACCOUNT_FORM), "Account form button is not presented"
        assert self.is_element_present(*AccountPageLocators.ACCOUNT_EXIT), "Account exit button is not presented"
        assert self.is_element_present(*AccountPageLocators.ACCOUNT_SAVE_BUTTON), "Account save button is not presented"

    def exit(self):
        self.should_be_account_form()
        exit_button = self.browser.find_element(*AccountPageLocators.ACCOUNT_EXIT)
        exit_button.click()
        login_page = LoginPage(self.browser, self.link)
        login_page.should_be_login_form()

    def not_editable_inputs(self):
        self.should_be_account_form()
        name_button = self.browser.find_element(*AccountPageLocators.ACCOUNT_INPUT)[0]
        name_button.send_keys("111111")
        assert name_button.text != "111111"
