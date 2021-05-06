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


class AccountPageLocators:
    ACCOUNT_FORM = (By.CSS_SELECTOR, ".card__employee__account")
    ACCOUNT_INPUT = (By.CSS_SELECTOR, ".card__employee__account-text")
    ACCOUNT_EXIT = (By.CSS_SELECTOR, ".card__employee__account__button-exit")
    ACCOUNT_PLUS_BUTTON = (By.CSS_SELECTOR, ".add-number__plus")
    ACCOUNT_SAVE_BUTTON = (By.CSS_SELECTOR, ".card__employee__numbers__button-save")
    ACCOUNT_PHONE = (By.CSS_SELECTOR, ".telephone-number-text")
    ACCOUNT_PHONE_MINUS_BUTTON = (By.CSS_SELECTOR, "#minus")
