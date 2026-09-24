import allure

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step('Открыть историю заказов')
    def open_order_history(self):
        self.click(AccountPageLocators.ORDER_HISTORY)
        self.wait_url_contains('/account/order-history')

    @allure.step('Выйти из аккаунта')
    def logout(self):
        self.click(AccountPageLocators.LOGOUT)
        self.wait_url_contains('/login')

    def is_order_in_history(self, number):
        self.wait_visible(AccountPageLocators.order(number))
        return True
