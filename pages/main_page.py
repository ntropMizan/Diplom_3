from pages.base_page import BasePage
import allure
from seletools.actions import drag_and_drop
import locators.main_page_locators


class MainFunctions(BasePage):
    @allure.step('Клик по кнопке "Конструктор"')
    def click_button_constructor(self):
        self.click(locators.main_page_locators.BUTTON_CONSTRUCTOR)

    @allure.step('Клик по ингредиенту"')
    def click_ingredient(self):
        self.click(locators.main_page_locators.INGREDIENT)

    @allure.step('Искать заголовок всплывающего окна')
    def wait_and_find_header(self):
        name = self.wait_and_find_element(locators.main_page_locators.POPUP_WINDOW_HEADER)
        return name

    @allure.step('Клик по крестику, чтобы закрыть всплывающее окно')
    def click_close_window(self):
        self.click(locators.main_page_locators.CLOSE_BUTTON)

    @allure.step('Найти невидимый крестик для закрытия окна')
    def cross_not_is_displayed(self):
        name = self.wait_and_find_element_invisible(locators.main_page_locators.CLOSE_BUTTON)
        return not name.is_displayed()

    @allure.step('Перетащить ингредиент в корзину покупателя')
    def put_ingredient_into_basket(self):
        ingredient = self.wait_and_find_element(locators.main_page_locators.INGREDIENT)
        basket = self.wait_and_find_element(locators.main_page_locators.ORDER_BASKET)
        drag_and_drop(self.driver, ingredient, basket)

    @allure.step('Искать текст по локатору ингредиента')
    def counter_ingredient_text(self):
        return self.find_text(locators.main_page_locators.INGREDIENT)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_make_order(self):
        self.click(locators.main_page_locators.BUTTON_MAKE_ORDER)

    @allure.step('Искать текст о подтверждении заказа')
    def wait_and_find_confirmation(self):
        name = self.wait_and_find_element(locators.main_page_locators.CONFIRMATION_TEXT)
        return name

    @allure.step('Клик по кнопке "Войти"')
    def click_enter_button(self):
        self.click(locators.main_page_locators.BUTTON_ENTER)

    @allure.step('Завершить логин пользователя и оформить заказ')
    def finish_login_and_make_order(self):
        self.click_enter_button()
        self.put_ingredient_into_basket()
        self.click_make_order()
