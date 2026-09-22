import allure

import data
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Открыть главную страницу')
    def open(self):
        self.open_url(data.BASE_URL)
        self.wait_visible(MainPageLocators.TITLE)

    @allure.step('Открыть детали ингредиента')
    def open_ingredient_details(self, name):
        self.script_click(MainPageLocators.ingredient(name))
        self.wait_visible(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step('Закрыть всплывающее окно')
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE)
        self.wait_invisible(MainPageLocators.MODAL)

    def ingredient_details_title(self):
        return self.get_text(MainPageLocators.INGREDIENT_DETAILS)

    def is_modal_closed(self):
        self.wait_invisible(MainPageLocators.MODAL)
        return True

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient(self, name):
        self.drag_and_drop(MainPageLocators.ingredient(name), MainPageLocators.BASKET)

    def ingredient_counter(self, name):
        return self.get_text(MainPageLocators.ingredient_counter(name))

    def wait_counter(self, name, previous):
        return self.wait_text_changes(MainPageLocators.ingredient_counter(name), previous)

    @allure.step('Оформить заказ')
    def place_order(self):
        self.click(MainPageLocators.ORDER_BUTTON)
        self.wait_visible(MainPageLocators.ORDER_CAPTION)
        return self.wait_order_number(MainPageLocators.ORDER_NUMBER)
