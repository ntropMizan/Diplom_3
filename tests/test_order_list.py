import allure
from pages.order_list_page import OrderList
from pages.personal_account_page import PersonalAccount


class TestOrderList:

    @allure.title('Открытие окна с заказом')
    @allure.description('Кликаем на "Ленту заказов", далее на любую карточку заказа, ждем открытия окна с заказом')
    def test_click_order_card(self, driver_both):
        test_order_list_page = OrderList(driver_both)
        test_order_list_page.click_order_list()
        test_order_list_page.wait_and_find_order_card()
        test_order_list_page.click_order_card()
        name = test_order_list_page.wait_and_find_order_card_window()
        assert name.is_displayed()

    @allure.title('Отображение сделанного заказа в ленте заказов')
    @allure.description('Логинюсь на сайте, оформляю заказ, смотрю номер заказа, иду в ленту заказа и ищу свой заказ')
    def test_make_order_and_check_order_list(self, default_user, driver_both):
        email = default_user["email"]
        password = default_user["password"]
        test_order_list_page = OrderList(driver_both)
        test_personal_account_page = PersonalAccount(driver_both)
        test_personal_account_page.click_button_personal_account()
        test_personal_account_page.set_email_input(email)
        test_personal_account_page.set_password_input(password)
        test_order_list_page.finish_login_make_order_close_window()
        test_order_list_page.enter_account_enter_profile_history()
        number_profile = test_order_list_page.number_text()
        test_order_list_page.click_order_list_and_wait_left_block()
        number_list = test_order_list_page.block_text()
        assert number_profile in number_list

    @allure.title('Увеличение счетчика "За все время" после оформления нового заказа')
    @allure.description('Логинимся, оформляю заказ и проверяю, что счетчик "За все время" увеличился')
    def test_counter_total_changes(self, default_user, driver_both):
        email = default_user["email"]
        password = default_user["password"]
        test_order_list_page = OrderList(driver_both)
        test_order_list_page.click_order_list_and_find_block_total()
        old_data = test_order_list_page.block_total_text()
        test_personal_account_page = PersonalAccount(driver_both)
        test_personal_account_page.click_button_personal_account()
        test_personal_account_page.set_email_input(email)
        test_personal_account_page.set_password_input(password)
        test_order_list_page.finish_login_make_order_close_window()
        test_order_list_page.click_order_list_and_find_block_total()
        new_data = test_order_list_page.block_total_text()
        assert int(new_data) > int(old_data)

    @allure.title('Увеличение счетчика "За сегодня" после оформления нового заказа')
    @allure.description('Логинимся, оформляю заказ и проверяю, что счетчик "За сегодня" увеличился')
    def test_counter_daily_changes(self, default_user, driver_both):
        email = default_user["email"]
        password = default_user["password"]
        test_order_list_page = OrderList(driver_both)
        test_order_list_page.click_order_list_find_block_daily()
        old_data = test_order_list_page.block_daily_text()
        test_personal_account_page = PersonalAccount(driver_both)
        test_personal_account_page.click_button_personal_account()
        test_personal_account_page.set_email_input(email)
        test_personal_account_page.set_password_input(password)
        test_order_list_page.finish_login_make_order_close_window()
        test_order_list_page.click_order_list_find_block_daily()
        new_data = test_order_list_page.block_daily_text()
        assert int(new_data) > int(old_data)

    @allure.title('Отображение созданного заказа в разделе "В работе"')
    @allure.description('Логинимся, оформляю заказ и проверяю, что заказ отобразился в разделе "В работе"')
    def test_make_order_and_check_order_in_work(self, default_user, driver_both):
        email = default_user["email"]
        password = default_user["password"]
        test_order_list_page = OrderList(driver_both)
        test_personal_account_page = PersonalAccount(driver_both)
        test_personal_account_page.click_button_personal_account()
        test_personal_account_page.set_email_input(email)
        test_personal_account_page.set_password_input(password)
        test_order_list_page.finish_login_make_order_close_window()
        test_order_list_page.enter_account_enter_profile_history()
        number_profile = test_order_list_page.number_text()
        test_order_list_page.click_order_list_find_in_work()
        number_in_work = test_order_list_page.number_in_work_text()
        assert number_in_work in (number_profile[1:]) or (str(int(number_profile[1:])-1))
