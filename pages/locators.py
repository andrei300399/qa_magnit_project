from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.login-main__container__card__login-form__button")
    LOGIN_FORM = (By.CSS_SELECTOR, "form.login-main__container__card__login-form")
    LOGIN_ALERT_EMPTY = (By.CSS_SELECTOR, "#login_alert_empty")
    LOGIN_ALERT_NOT_EXIST_USER = (By.CSS_SELECTOR, "#login_alert_not_exist_user")


class AdminPageLocators:
    pass


class AccountPageLocators:
    ACCOUNT_FORM = (By.CSS_SELECTOR, "#account_form")
    ACCOUNT_NAME = (By.CSS_SELECTOR, "#account_name")
    ACCOUNT_DATE = (By.CSS_SELECTOR, "#account_date")
    ACCOUNT_MAIL = (By.CSS_SELECTOR, "#account_mail")
    ACCOUNT_JOB = (By.CSS_SELECTOR, "#account_job")
    ACCOUNT_WORKPLACE = (By.CSS_SELECTOR, "#account_workplace")
    ACCOUNT_EXIT = (By.CSS_SELECTOR, "#account_exit")
    ACCOUNT_PLUS_BUTTON = (By.CSS_SELECTOR, "#account_plus_button")
    ACCOUNT_SAVE_BUTTON = (By.CSS_SELECTOR, "#account_save_button")
    ACCOUNT_PHONE = (By.CSS_SELECTOR, "#account_phone")
