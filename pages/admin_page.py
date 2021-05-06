from .base_page import BasePage
from .locators import AdminPageLocators


class AdminPage(BasePage):
    def should_be_admin_table(self):
        assert self.is_element_present(*AdminPageLocators.ADMIN_BUTTON_LOAD), "Admin load button is not presented"
        assert self.is_element_present(*AdminPageLocators.ADMIN_TABLE), "Admin table is not presented"
        assert self.is_element_present(*AdminPageLocators.ADMIN_BUTTON_SAVE), "Admin save button is not presented"
        assert self.is_element_present(*AdminPageLocators.ADMIN_BUTTON_ADD_USER), "Admin save button is not presented"
        assert self.is_element_present(*AdminPageLocators.ADMIN_LINK_TO_LK), "Admin link to lk is not presented"
        assert self.is_element_present(*AdminPageLocators.ADMIN_FORM_SEARCH), "Admin search form is not presented"

    def add_user(self):
        self.should_be_admin_table()


