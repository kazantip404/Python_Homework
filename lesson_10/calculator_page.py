from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CalculatorPage:
    """Page Object для страницы калькулятора с задержкой вычислений."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CLASS_NAME, "screen")
        self.buttons = {
            "7": (By.XPATH, "//span[text()='7']"),
            "8": (By.XPATH, "//span[text()='8']"),
            "+": (By.XPATH, "//span[text()='+']"),
            "=": (By.XPATH, "//span[text()='=']")
        }

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, delay: str) -> None:
        """
        Устанавливает время задержки вычислений.

        Args:
            delay: Время задержки в секундах (строка)
        """
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(delay)

    def click_button(self, button: str) -> None:
        """
        Нажимает указанную кнопку калькулятора.

        Args:
            button: Идентификатор кнопки ('7', '8', '+', '=')
        """
        self.driver.find_element(*self.buttons[button]).click()

    def get_result(self, timeout: int = 52) -> str:
        """
        Ожидает и возвращает результат вычислений.

        Args:
            timeout: Максимальное время ожидания в секундах

        Returns:
            Текст результата вычислений
        """
        result_element = self.driver.find_element(*self.screen)
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda driver: result_element.text == "15")
        return result_element.text