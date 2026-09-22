from selenium.webdriver.common.by import By


class FeedPageLocators:
    TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    TOTAL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TOTAL_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    FIRST_ORDER = (By.XPATH, "(//a[contains(@href, '/feed/')])[1]")
    FIRST_ORDER_NUMBER = (By.XPATH, "(//a[contains(@href, '/feed/')])[1]//p[contains(@class, 'digits-default')]")
    ORDER_COMPOSITION = (
        By.XPATH,
        "//*[contains(@class, 'Modal_modal_opened')]//p[contains(text(), 'остав')]",
    )

    @staticmethod
    def order(number):
        return (
            By.XPATH,
            f"//a[contains(@href, '/feed/')][.//p[text()='#0{number}']]",
        )

    @staticmethod
    def ready_order(number):
        return (
            By.XPATH,
            "//ul[contains(@class, 'OrderFeed_orderList__') and "
            "not(contains(@class, 'orderListReady'))]"
            f"//li[normalize-space(.)='0{number}']",
        )
