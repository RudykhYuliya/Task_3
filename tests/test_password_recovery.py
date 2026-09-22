import allure


class TestPasswordRecovery:
    @allure.title('Можно перейти на страницу восстановления пароля')
    def test_open_password_recovery(self, login_page, forgot_password_page):
        login_page.open()
        login_page.click_recover_password()
        forgot_password_page.wait_url_contains('/forgot-password')
        assert forgot_password_page.title() == 'Восстановление пароля'

    @allure.title('Можно ввести почту и нажать Восстановить')
    def test_submit_recovery_email(self, login_page, forgot_password_page):
        login_page.open()
        login_page.click_recover_password()
        forgot_password_page.recover('julia_recover@yandex.ru')
        assert '/reset-password' in forgot_password_page.get_current_url()

    @allure.title('Кнопка показать пароль подсвечивает поле')
    def test_show_password_highlights_field(self, login_page, forgot_password_page, reset_password_page):
        login_page.open()
        login_page.click_recover_password()
        forgot_password_page.recover('julia_recover@yandex.ru')
        reset_password_page.show_password()
        assert reset_password_page.is_password_field_active()
