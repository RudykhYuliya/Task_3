import allure

import data


class TestMain:
    @allure.title('Можно перейти в конструктор')
    def test_open_constructor(self, main_page):
        main_page.click_order_feed()
        main_page.click_constructor()
        assert main_page.get_current_url().rstrip('/') == data.BASE_URL.rstrip('/')

    @allure.title('Можно перейти в ленту заказов')
    def test_open_order_feed(self, main_page):
        main_page.click_order_feed()
        assert '/feed' in main_page.get_current_url()

    @allure.title('Клик по ингредиенту открывает окно с деталями')
    def test_ingredient_details_modal(self, main_page):
        main_page.open_ingredient_details(data.BUN)
        assert main_page.ingredient_details_title() == 'Детали ингредиента'

    @allure.title('Окно с деталями ингредиента закрывается по крестику')
    def test_close_ingredient_details(self, main_page):
        main_page.open_ingredient_details(data.BUN)
        main_page.close_modal()
        assert main_page.is_modal_closed()

    @allure.title('Счетчик ингредиента увеличивается при добавлении в заказ')
    def test_ingredient_counter_increases(self, main_page):
        before = main_page.ingredient_counter(data.SAUCE)
        main_page.add_ingredient(data.SAUCE)
        after = main_page.wait_counter(data.SAUCE, before)
        assert int(after) > int(before)

    @allure.title('Авторизованный пользователь может оформить заказ')
    def test_authorized_user_can_place_order(self, user, main_page, login_page):
        main_page.click_account()
        login_page.login(user['email'], user['password'])
        main_page.add_ingredient(data.BUN)
        main_page.add_ingredient(data.SAUCE)
        number = main_page.place_order()
        assert number.isdigit()
