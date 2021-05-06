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
        name_button = self.browser.find_elements(*AccountPageLocators.ACCOUNT_INPUT)[0]
        try:
            name_button.send_keys("111111")
        except:
            assert name_button.text != "111111"
        else:
            assert False

    def right_add_or_remove_phone_inputs(self):
        self.should_be_account_form()
        phones_input = self.browser.find_elements(*AccountPageLocators.ACCOUNT_PHONE)
        if len(phones_input) < 5:
            plus_button = self.browser.find_element(*AccountPageLocators.ACCOUNT_PLUS_BUTTON)
            plus_button.click()
            phones_input_after_add = self.browser.find_elements(*AccountPageLocators.ACCOUNT_PHONE)
            assert len(phones_input) == len(phones_input_after_add) - 1
        else:
            minus_button = self.browser.find_element(*AccountPageLocators.ACCOUNT_PHONE_MINUS_BUTTON)
            minus_button.click()
            phones_input_after_remove = self.browser.find_elements(*AccountPageLocators.ACCOUNT_PHONE)
            assert len(phones_input) - 1 == len(phones_input_after_remove)
