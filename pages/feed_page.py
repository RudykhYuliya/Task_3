import allure

import data
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step('Открыть ленту заказов')
    def open(self):
        self.open_url(data.BASE_URL + '/feed')
        self.wait_visible(FeedPageLocators.TITLE)

    def total(self):
        return int(self.wait_digits(FeedPageLocators.TOTAL))

    def total_today(self):
        return int(self.wait_digits(FeedPageLocators.TOTAL_TODAY))

    def wait_total_greater_than(self, previous):
        self.wait_number_greater_than(FeedPageLocators.TOTAL, previous)

    def wait_total_today_greater_than(self, previous):
        self.wait_number_greater_than(FeedPageLocators.TOTAL_TODAY, previous)

    @allure.step('Открыть заказ в ленте')
    def open_first_order(self):
        number = self.get_text(FeedPageLocators.FIRST_ORDER_NUMBER)
        self.script_click(FeedPageLocators.FIRST_ORDER)
        self.wait_visible(FeedPageLocators.ORDER_COMPOSITION)
        return number

    def is_order_in_feed(self, number):
        self.wait_visible(FeedPageLocators.order(number))
        return True

    def is_order_ready(self, number):
        self.wait_visible(FeedPageLocators.ready_order(number))
        return True
