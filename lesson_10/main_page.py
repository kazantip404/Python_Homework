from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    """Page Object для главной страницы магазина."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация главной страницы.

        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")
        self.items = {
            "backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "bolt_t_shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "onesie": (By.ID, "add-to-cart-sauce-labs-onesie")
        }

    def add_item_to_cart(self, item_name: str) -> None:
        """
        Добавляет товар в корзину.

        Args:
            item_name: Название товара для добавления
        """
        self.driver.find_element(*self.items[item_name]).click()

    def go_to_cart(self) -> None:
        """Переходит в корзину покупок."""
        self.driver.find_element(*self.cart_button).click()