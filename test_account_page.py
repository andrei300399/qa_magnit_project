from .pages.account_page import AccountPage
from .pages.login_page import LoginPage

USER_LOGIN = "test_user@magnitversion2.onmicrosoft.com"
USER_PASSWORD = "Docu4647123"


def test_exit_from_account(browser):
    link = "/"
    page = LoginPage(browser, link)
    page.open()
    page.authorization_exist_user(USER_LOGIN, USER_PASSWORD)
    link = "http://localhost:8080/lk"
    page = AccountPage(browser, link)
    page.exit()


