import time

from .base_page import BasePage
from .locators import AdminPageLocators
from selenium.webdriver import ActionChains

name, last, middle, department, post = "qqqqq", "qqqqq", "qqqqq", "qqqqq", "qqqqq"
phone, date = "555555555", "55555555"
email = "5555@amail.ru"


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
        button = self.browser.find_element(*AdminPageLocators.ADMIN_BUTTON_ADD_USER)
        button.click()
        name_input = self.browser.find_element(*AdminPageLocators.ADMIN_ADD_USER_FIRSTNAME)
        name_input.send_keys(name)
        last_name_input = self.browser.find_element(*AdminPageLocators.ADMIN_ADD_USER_LASTNAME)
        last_name_input.send_keys(last)
        mid_name_input = self.browser.find_element(*AdminPageLocators.ADMIN_ADD_USER_MIDDLENAME)
        mid_name_input.send_keys(middle)
        department_input = self.browser.find_element(*AdminPageLocators.ADMIN_ADD_USER_DEPARTMENT)
        department_input.send_keys(department)
        date_input = self.browser.find_element(*AdminPageLocators.ADMIN_ADD_USER_DATE)
        date_input.send_keys(date)
        post_input = self.browser.find_element(*AdminPageLocators.ADMIN_ADD_USER_POST)
        post_input.send_keys(post)
        button_add = self.browser.find_element(*AdminPageLocators.ADMIN_ADD_USER_PLUS_BUTTON)
        button_add.click()
        phone_input = self.browser.find_element(*AdminPageLocators.ADMIN_ADD_USER_PHONE_INPUT)
        phone_input.send_keys(phone)
        email_input = self.browser.find_element(*AdminPageLocators.ADMIN_ADD_USER_EMAIL)
        email_input.send_keys(email)
        button_save = self.browser.find_element(*AdminPageLocators.ADMIN_ADD_USER_SAVE_BUTTON)
        button_save.click()
        button_confirm = self.browser.find_element(*AdminPageLocators.ADMIN_ADD_CONFIRM_YES)
        button_confirm.click()

    def remove_user(self, last_name):
        self.should_be_admin_table()
        time.sleep(5)
        search_input = self.browser.find_element(*AdminPageLocators.ADMIN_SEARCH_INPUT)
        search_input.send_keys(last_name)
        search_button = self.browser.find_element(*AdminPageLocators.ADMIN_SEARCH_BUTTON)
        search_button.click()
        row_user = self.browser.find_element(*AdminPageLocators.ADMIN_ROW_USER)
        action = ActionChains(self.browser)
        action.context_click(row_user).perform()
        delete_button = self.browser.find_element(*AdminPageLocators.ADMIN_BUTTON_DELETE)
        delete_button.click()
        button_confirm = self.browser.find_element(*AdminPageLocators.ADMIN_ADD_CONFIRM_YES)
        button_confirm.click()
        assert self.is_element_present(*AdminPageLocators.ADMIN_NOT_FOUND)

