from selenium.webdriver.common.by import By


class AccountPageLocators:
    ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT = (By.XPATH, "//button[text()='Выход']")

    @staticmethod
    def order(number):
        return (
            By.XPATH,
            f"//a[contains(@href, '/account/order-history/')][.//p[text()='#0{number}']]",
        )
