import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def title(self):
        return self.get_text(ForgotPasswordPageLocators.TITLE)

    @allure.step('Ввести почту и нажать Восстановить')
    def recover(self, email):
        self.set_value(ForgotPasswordPageLocators.EMAIL, email)
        self.click(ForgotPasswordPageLocators.RECOVER_BUTTON)
        self.wait_url_contains('/reset-password')
