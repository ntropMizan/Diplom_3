from selenium.webdriver.common.by import By

BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
INGREDIENT = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']/div/p[@class='counter_counter__num__3nue1']")
POPUP_WINDOW_HEADER = (By.XPATH, "//h2[text()='Детали ингредиента']")
CLOSE_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
ORDER_BASKET = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
BUTTON_MAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
CONFIRMATION_TEXT = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")
