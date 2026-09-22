import allure

import data


class TestOrderFeed:
    @allure.title('Клик по заказу открывает окно с деталями')
    def test_order_details_modal(self, feed_page):
        feed_page.open()
        number = feed_page.open_first_order()
        assert number.startswith('#')

    @allure.title('Заказ из истории отображается в ленте заказов')
    def test_user_order_is_in_feed(self, user, main_page, login_page, account_page, feed_page):
        main_page.click_account()
        login_page.login(user['email'], user['password'])
        main_page.add_ingredient(data.BUN)
        main_page.add_ingredient(data.SAUCE)
        number = main_page.place_order()
        main_page.close_modal()
        main_page.click_account()
        account_page.open_order_history()
        assert account_page.is_order_in_history(number)
        feed_page.open()
        assert feed_page.is_order_in_feed(number)

    @allure.title('Счетчик Выполнено за все время увеличивается')
    def test_total_increases(self, user, main_page, login_page, feed_page):
        feed_page.open()
        total = feed_page.total()
        main_page.open()
        main_page.click_account()
        login_page.login(user['email'], user['password'])
        main_page.add_ingredient(data.BUN)
        main_page.add_ingredient(data.SAUCE)
        main_page.place_order()
        feed_page.open()
        feed_page.wait_total_greater_than(total)
        assert feed_page.total() > total

    @allure.title('Счетчик Выполнено за сегодня увеличивается')
    def test_total_today_increases(self, user, main_page, login_page, feed_page):
        feed_page.open()
        total_today = feed_page.total_today()
        main_page.open()
        main_page.click_account()
        login_page.login(user['email'], user['password'])
        main_page.add_ingredient(data.BUN)
        main_page.add_ingredient(data.SAUCE)
        main_page.place_order()
        feed_page.open()
        feed_page.wait_total_today_greater_than(total_today)
        assert feed_page.total_today() > total_today

    @allure.title('Номер оформленного заказа появляется в колонке Готовы')
    def test_order_number_appears_in_ready(self, user, main_page, login_page, feed_page):
        main_page.click_account()
        login_page.login(user['email'], user['password'])
        main_page.add_ingredient(data.BUN)
        main_page.add_ingredient(data.SAUCE)
        number = main_page.place_order()
        feed_page.open()
        assert feed_page.is_order_ready(number)
