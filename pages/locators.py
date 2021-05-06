from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a.login-main__container__card__login-form__button")
    LOGIN_FORM = (By.CSS_SELECTOR, "form.login-main__container__card__login-form")
    LOGIN_ALERT_EMPTY = (By.CSS_SELECTOR, "#login_alert_empty")
    LOGIN_ALERT_NOT_EXIST_USER = (By.CSS_SELECTOR, "#login_alert_not_exist_user")
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, "input[type='email']")
    LOGIN_FORM_BUTTON_MS = (By.CSS_SELECTOR, "input[type='submit']")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON_MS_CONTINUE = (By.CSS_SELECTOR, ".form-group a")
    LOGIN_BUTTON_APP_CONTINUE = (By.CSS_SELECTOR, ".continue-confirm-message-frame__button-ok")
    LOGIN_BUTTON_NOT_EXIT = (By.CSS_SELECTOR, "#idSIButton9")
    LOGIN_NAME_IN_LK = (By.CSS_SELECTOR, ".card__employee__account-text")
    LOGIN_ERROR_TO_HOME = (By.CSS_SELECTOR, "li a")
    LOGIN_BTN_LOG = (By.CSS_SELECTOR, ".btn.btn-primary")


class AdminPageLocators:
    ADMIN_TABLE = (By.CSS_SELECTOR, ".content-table")
    ADMIN_BUTTON_SAVE = (By.CSS_SELECTOR, ".main__menu__form__btn.btn-save")
    ADMIN_BUTTON_ADD_USER = (By.CSS_SELECTOR, ".main__menu__form__btn.btn-add")
    ADMIN_BUTTON_LOAD = (By.CSS_SELECTOR, ".main__menu__form__btn.btn-export")
    ADMIN_FORM_SEARCH = (By.CSS_SELECTOR, ".main__menu__form__search")
    ADMIN_LINK_TO_LK = (By.CSS_SELECTOR, ".nav__list__item__account")
    ADMIN_ADD_USER_LASTNAME = (By.CSS_SELECTOR, "input[name='lastname']")
    ADMIN_ADD_USER_FIRSTNAME = (By.CSS_SELECTOR, "input[name='number']")
    ADMIN_ADD_USER_MIDDLENAME = (By.CSS_SELECTOR, "input[name='middlename']")
    ADMIN_ADD_USER_EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    ADMIN_ADD_USER_POST = (By.CSS_SELECTOR, "input[name='post']")
    ADMIN_ADD_USER_DATE = (By.CSS_SELECTOR, "input[name='dateOfBirth']")
    ADMIN_ADD_USER_DEPARTMENT = (By.CSS_SELECTOR, "input[name='department']")
    ADMIN_ADD_USER_SAVE_BUTTON = (By.CSS_SELECTOR, ".edit__card__employee__numbers__button-save")
    ADMIN_ADD_USER_PLUS_BUTTON = (By.CSS_SELECTOR, ".edit__card__employee__numbers__add-number")
    ADMIN_ADD_USER_PHONE_INPUT = (By.CSS_SELECTOR, ".edit__telephone-number-text")
    ADMIN_ADD_CONFIRM_YES = (By.CSS_SELECTOR, ".confirm-message-frame__button-yes")
    ADMIN_SEARCH_INPUT = (By.CSS_SELECTOR, ".main__menu__form__search__input")
    ADMIN_SEARCH_BUTTON = (By.CSS_SELECTOR, ".main__menu__form__btn-search-img")
    ADMIN_ROW_USER = (By.CSS_SELECTOR, ".content-table tbody tr")
    ADMIN_BUTTON_DELETE = (By.CSS_SELECTOR, ".context-menu__option__delete")
    ADMIN_NOT_FOUND = (By.CSS_SELECTOR, ".main__table__not-found")




class AccountPageLocators:
    ACCOUNT_FORM = (By.CSS_SELECTOR, ".card__employee__account")
    ACCOUNT_INPUT = (By.CSS_SELECTOR, ".card__employee__account-text")
    ACCOUNT_EXIT = (By.CSS_SELECTOR, ".card__employee__account__button-exit")
    ACCOUNT_PLUS_BUTTON = (By.CSS_SELECTOR, ".add-number__plus")
    ACCOUNT_SAVE_BUTTON = (By.CSS_SELECTOR, ".card__employee__numbers__button-save")
    ACCOUNT_PHONE = (By.CSS_SELECTOR, ".telephone-number-text")
    ACCOUNT_PHONE_MINUS_BUTTON = (By.CSS_SELECTOR, "#minus")
