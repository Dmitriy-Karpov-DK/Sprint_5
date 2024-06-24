from selenium.webdriver.common.by import By


class Locators:
    ACCOUNT_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка войти в аккаунт
    NAME_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # поле ввода имя
    NAME_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # поле ввода email
    PASSWORD = (By.XPATH, "//input[@name='Пароль']")  # поле ввода пароль
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # кнопка выхода из аккаунта
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка входа в аккаунт
    TITLE_PERSONAL_ACCOUNT = (By.XPATH, "//a[@href='/account']")  # заголовок Личный Кабинет
    AUTH_LOGIN_ELEMENT = (By.CLASS_NAME, "Auth_login__3hAey")  # элемент авторизации
    INPUT_ELEMENT = (By.XPATH, "//input")  # элемент поля ввода
    CONSTRUCTOR_ELEMENT = (By.XPATH, "//*[@class='BurgerIngredients_ingredients__1N8v2']")  # страница конструктора
    ELEMENT_PERSONAL_ACCOUNT = (By.CLASS_NAME, "Account_contentBox__2CPm3")  # страница личного кабинета
    ELEMENT_AUTH_FORM = (By.CLASS_NAME, "Auth_form__3qKeq mb-20")  # элемент формы регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка Зарегистрироваться
    LOGIN_BUTTON_IN_REGISTER = (By.XPATH, "//a[@href='/login']")  # кнопка Войти в форме регистрации
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//a[@href='/forgot-password']")  # кнопка Восстановить пароль
    LOGIN_BUTTON_IN_RECOVER_PASSWORD = (By.XPATH, "//a[@href='/login']")  # кнопка Войти в форме восстановления пароля
    REGISTER_BUTTON_LINK = (By.XPATH, "//a[@href='/register']")  # ссылка на страницу регистрации
    TITLE_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # заголовок Конструктор
    TITLE_STELLAR_BURGERS = (By.XPATH, "//a[@href='/']")  # заголовок stellar burgers
    EXIT_BUTTON_IN_PERS_ACC = (By.XPATH, "//button[text()='Выход']")  # кнопка Выход в личном кабинете
    GO_TO_BREAD = (By.XPATH, "//span[text()='Булки']")  # переход в раздел Булки
    GO_TO_SAUCES = (By.XPATH, "//span[text()='Соусы']")  # переход в раздел Соусы
    GO_TO_FILLING = (By.XPATH, "//span[text()='Начинки']")  # переход к разделу Начинки
    TITLE_BREAD = (By.XPATH, "//h2[text()='Булки']")  # заголовок Булки
    TITLE_FILLING = (By.XPATH, "//h2[text()='Начинки']")  # заголовок Начинки
    TITLE_SAUCES = (By.XPATH, "//h2[text()='Соусы']")  # заголовок Соусы
