from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RECOVER_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")
