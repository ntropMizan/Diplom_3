import allure
from pages.password_recovery_page import PasswordRecoveryPage
from data import URL


class TestPasswordRecoveryPage:

    @allure.title('Переход на страницу восстановления пароля')
    @allure.description('Проверяем, что по кнопке "Восстановить пароль" мы попадаем на страницу восстановления пароля')
    def test_get_reset_password_page(self, driver_both):
        test_reset_password_page = PasswordRecoveryPage(driver_both)
        test_reset_password_page.enter_and_click_reset_password()
        assert test_reset_password_page.get_current_url() == URL.BASE_PAGE + URL.FORGOT_PASSWORD_PAGE

    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    @allure.description('Проверяем, что можно заполнить поле почты и отправить данные по кнопке "Восстановить"')
    def test_input_email_and_reset(self, driver_both):
        test_reset_password_page = PasswordRecoveryPage(driver_both)
        test_reset_password_page.enter_and_click_reset_password()
        test_reset_password_page.set_email_and_click_restore_button()
        test_reset_password_page.wait_for_url_changes_restore()
        assert test_reset_password_page.get_current_url() == URL.BASE_PAGE + URL.RESET_PASSWORD_PAGE

    @allure.title('Активация поля для восстановления пароля через клик по "глазу"')
    @allure.description('Проверяем, что кликнув на "глаз" в поле ввода пароля, само поле становится активным')
    def test_active_password_field(self, driver_both):
        test_reset_password_page = PasswordRecoveryPage(driver_both)
        test_reset_password_page.enter_and_click_reset_password()
        test_reset_password_page.set_email_and_click_restore_button()
        test_reset_password_page.wait_for_url_changes_restore()
        non_active = test_reset_password_page.get_input_status()
        test_reset_password_page.click_the_aye()
        active = test_reset_password_page.get_input_status()
        assert (non_active is False and active is True)
