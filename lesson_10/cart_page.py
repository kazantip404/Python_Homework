from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Page Object для страницы корзины покупок."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def checkout(self) -> None:
        """Нажимает кнопку оформления заказа."""
        self.driver.find_element(*self.checkout_button).click()