from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    ORDER_FEED = (By.XPATH, "//a[.//p[text()='Лента Заказов']]")
    ACCOUNT = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")
