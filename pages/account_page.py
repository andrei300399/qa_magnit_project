from .base_page import BasePage
from .locators import AccountPageLocators


class AccountPage(BasePage):
    def should_be_account_form(self):
        assert self.is_element_present(*AccountPageLocators.ACCOUNT_FORM), "Account form is not presented"
        assert self.is_element_present(*AccountPageLocators.ACCOUNT_JOB), "Account job is not presented"
        assert self.is_element_present(*AccountPageLocators.ACCOUNT_EXIT), "Account exit button is not presented"
        assert self.is_element_present(*AccountPageLocators.ACCOUNT_DATE), "Account bith date is not presented"
        assert self.is_element_present(*AccountPageLocators.ACCOUNT_MAIL), "Account mail is not presented"
        assert self.is_element_present(*AccountPageLocators.ACCOUNT_NAME), "Account name is not presented"
        assert self.is_element_present(*AccountPageLocators.ACCOUNT_WORKPLACE), "Account workplace is not presented"
        assert self.is_element_present(*AccountPageLocators.ACCOUNT_SAVE_BUTTON), "Account save button is not presented"

    def exit(self):
        self.should_be_account_form()
        exit_button = self.browser.find_element(*AccountPageLocators.ACCOUNT_EXIT)
        exit_button.click()

    def not_editable_inputs(self):
        self.should_be_account_form()
        name_button = self.browser.find_element(*AccountPageLocators.ACCOUNT_NAME)
        name_button.send("111111")

