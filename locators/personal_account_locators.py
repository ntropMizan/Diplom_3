from selenium.webdriver.common.by import By

BUTTON_ACCOUNT = (By.XPATH, "//*[contains(text(), 'Личный Кабинет')]")
BUTTON_HISTORY_PROFILE = (By.XPATH, "//a[text()='История заказов']")
BUTTON_SAVE = \
    (By.XPATH,
     "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
INPUT_EMAIL = (By.XPATH, "//label[text() = 'Email']/../input")
INPUT_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/../input")
BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")
EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
