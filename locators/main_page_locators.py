from selenium.webdriver.common.by import By


class MainPageLocators:
    TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    BASKET = (By.CSS_SELECTOR, "[class*='BurgerConstructor_basket']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL = (By.CSS_SELECTOR, "[class*='Modal_modal_opened']")
    MODAL_CLOSE = (
        By.XPATH,
        "//*[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]",
    )
    ORDER_NUMBER = (
        By.XPATH,
        "//*[contains(@class, 'Modal_modal_opened')]//h2[contains(@class, 'text_type_digits-large')]",
    )
    ORDER_CAPTION = (By.XPATH, "//p[text()='идентификатор заказа']")

    @staticmethod
    def ingredient(name):
        return (
            By.XPATH,
            f"//a[contains(@class, 'BurgerIngredient_ingredient') and .//p[text()='{name}']]",
        )

    @staticmethod
    def ingredient_counter(name):
        return (
            By.XPATH,
            "//a[contains(@class, 'BurgerIngredient_ingredient') and "
            f".//p[text()='{name}']]//p[contains(@class, 'counter__num')]",
        )
