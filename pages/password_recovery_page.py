from data import ITEMS
from data import URL
from pages.base_page import BasePage
import allure
import locators.password_recovery_page_locators


class PasswordRecoveryPage(BasePage):

    @allure.step('клик по кнопке "Входа в аккаунт"')
    def click_button_enter_account(self):
        self.click(locators.password_recovery_page_locators.BUTTON_ENTER_ACCOUNT)

    @allure.step('клик по кнопке "Восстановить пароль')
    def click_reset_password(self):
        self.click(locators.password_recovery_page_locators.BUTTON_RESET_PASSWORD)

    @allure.step('Клик по кнопке "Входа в аккаунт" + клик по кнопке "Восстановить пароль"')
    def enter_and_click_reset_password(self):
        self.click_button_enter_account()
        self.click_reset_password()

    @allure.step('Заполнение поля почты')
    def set_email_input(self, email):
        email_input = self.wait_and_find_element(locators.password_recovery_page_locators.EMAIL_FIELD)
        email_input.send_keys(email)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_button_restore_password(self):
        self.click(locators.password_recovery_page_locators.RESTORE_BUTTON)

    @allure.step('Заполнение поля почты + клик по кнопке "Восстановить"')
    def set_email_and_click_restore_button(self):
        self.set_email_input(ITEMS.email)
        self.click_button_restore_password()

    @allure.step('Ожидание смены веб-странички с восстановлением пароля')
    def wait_for_url_changes_restore(self):
        self.wait_url_changes(URL.BASE_PAGE + URL.FORGOT_PASSWORD_PAGE)

    @allure.step('Получение и возврат атрибута вида "тип" со значением "текст"')
    def get_input_status(self):
        input_status = self.wait_and_find_element(locators.password_recovery_page_locators.PASSWORD_FIELD)
        return input_status.get_attribute("type") == 'text'

    @allure.step('Клик по "глазу" в поле ввода пароля')
    def click_the_aye(self):
        self.click(locators.password_recovery_page_locators.CLICK_AYE_AREA)
