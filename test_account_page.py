from .pages.account_page import AccountPage
from .pages.login_page import LoginPage
import pytest

USER_LOGIN = "test_user@magnitversion2.onmicrosoft.com"
USER_PASSWORD = "Docu4647123"


@pytest.fixture
def login_page(browser):
    link = "/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.authorization_exist_user(USER_LOGIN, USER_PASSWORD)
    yield login_page


@pytest.fixture(scope="function", autouse=True)
def account_page(browser):
    link = "/lk"
    account_page = AccountPage(browser, link)
    yield account_page


def test_exit_from_account(account_page):
    account_page.exit()


def test_editable_account(account_page):
    account_page.not_editable_inputs()


def test_right_remove_add_phone_inputs(account_page):
    account_page.right_add_or_remove_phone_inputs()
