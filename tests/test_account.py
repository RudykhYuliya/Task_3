import allure


class TestAccount:
    @allure.title('Можно перейти в личный кабинет')
    def test_open_account(self, user, main_page, login_page):
        main_page.click_account()
        login_page.login(user['email'], user['password'])
        main_page.click_account()
        main_page.wait_url_contains('/account/profile')
        assert '/account/profile' in main_page.get_current_url()

    @allure.title('Можно перейти в историю заказов')
    def test_open_order_history(self, user, main_page, login_page, account_page):
        main_page.click_account()
        login_page.login(user['email'], user['password'])
        main_page.click_account()
        account_page.open_order_history()
        assert '/account/order-history' in account_page.get_current_url()

    @allure.title('Можно выйти из аккаунта')
    def test_logout(self, user, main_page, login_page, account_page):
        main_page.click_account()
        login_page.login(user['email'], user['password'])
        main_page.click_account()
        account_page.logout()
        assert '/login' in account_page.get_current_url()
