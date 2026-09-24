import pytest
from selenium import webdriver

import helpers
from pages.account_page import AccountPage
from pages.feed_page import FeedPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    else:
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1400,1000')
        browser = webdriver.Chrome(options=options)
    browser.set_window_size(1400, 1000)
    yield browser
    browser.quit()


@pytest.fixture
def user():
    payload = helpers.generate_user()
    response = helpers.register_user(payload)
    payload['accessToken'] = response.json()['accessToken']
    yield payload
    helpers.delete_user(payload['accessToken'])


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open()
    return page


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)


@pytest.fixture
def reset_password_page(driver):
    return ResetPasswordPage(driver)


@pytest.fixture
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture
def feed_page(driver):
    return FeedPage(driver)
