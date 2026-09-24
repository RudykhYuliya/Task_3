import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step('Нажать показать или скрыть пароль')
    def show_password(self):
        self.click(ResetPasswordPageLocators.SHOW_PASSWORD)
        self.wait_for_class(ResetPasswordPageLocators.PASSWORD_FIELD, 'input_status_active')

    def is_password_field_active(self):
        self.wait_for_class(ResetPasswordPageLocators.PASSWORD_FIELD, 'input_status_active')
        return True
