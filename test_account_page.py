from .pages.account_page import AccountPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://localhost:8080/account"
    page = AccountPage(browser, link)
    page.open()
    time.sleep(3)


