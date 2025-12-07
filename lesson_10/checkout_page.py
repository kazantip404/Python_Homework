from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.

        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет информацию для оформления заказа.

        Args:
            first_name: Имя покупателя
            last_name: Фамилия покупателя
            postal_code: Почтовый индекс
        """
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.postal_code_field).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_amount(self) -> str:
        """
        Получает итоговую сумму заказа.

        Returns:
            Текст с итоговой суммой
        """
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_label)
        )
        return total_element.text