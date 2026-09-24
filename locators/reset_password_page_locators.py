from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']/parent::div")
    SHOW_PASSWORD = (By.CSS_SELECTOR, ".input__icon-action")
