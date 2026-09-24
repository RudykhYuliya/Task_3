import allure

import data
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Открыть страницу входа')
    def open(self):
        self.open_url(data.BASE_URL + '/login')
        self.wait_visible(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Нажать Восстановить пароль')
    def click_recover_password(self):
        self.click(LoginPageLocators.RECOVER_PASSWORD)

    @allure.step('Войти')
    def login(self, email, password):
        self.set_value(LoginPageLocators.EMAIL, email)
        self.set_value(LoginPageLocators.PASSWORD, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.wait_url_is(data.BASE_URL)
