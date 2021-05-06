from .pages.admin_page import AdminPage
from .pages.login_page import LoginPage
import pytest

ADMIN_LOGIN = "test_admin@magnitversion2.onmicrosoft.com"
ADMIN_PASSWORD = "Duju5262123"


@pytest.fixture(autouse=True)
def admin_page(browser):
    link = "/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.authorization_exist_user(ADMIN_LOGIN, ADMIN_PASSWORD)
    link = "/numbers"
    admin_page = AdminPage(browser, link)
    admin_page.open()
    yield admin_page


def test_add_user(admin_page):
    admin_page.add_user()
