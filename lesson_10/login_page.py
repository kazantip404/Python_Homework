from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Page Object для страницы авторизации."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы логина.

        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self) -> None:
        """Открывает страницу авторизации."""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему.

        Args:
            username: Логин пользователя
            password: Пароль пользователя
        """
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()