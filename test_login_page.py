import pytest

from .pages.login_page import LoginPage


@pytest.fixture(scope="function", autouse=True)
def setup(self, browser):
    link = "/login"
    page = LoginPage(browser, link)
    page.open()
    yield page


def test_authorization_user(page):
    page.authorization_exist_user()


def test_empty_authorization(page):
    page.authorization_empty_form()

def test_not_exist_user_authorization(page):
    page.authorization_not_exist_user()
