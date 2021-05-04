import pytest
import time

from .pages.login_page import LoginPage

USER_LOGIN = "test_user@magnitversion2.onmicrosoft.com"
USER_PASSWORD = "Docu4647123"


@pytest.fixture(scope="function", autouse=True)
def page(browser):
    link = "/"
    page = LoginPage(browser, link)
    page.open()
    yield page


def test_authorization_user(page):
    page.authorization_exist_user(USER_LOGIN, USER_PASSWORD)

