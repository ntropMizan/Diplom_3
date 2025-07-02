from selenium.webdriver.common.by import By


BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
BUTTON_RESET_PASSWORD = (By.XPATH, "//*[contains(@href,'/forgot-password')]")
EMAIL_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")
CLICK_AYE_AREA = (By.XPATH, "//div[@class='input__icon input__icon-action']")
