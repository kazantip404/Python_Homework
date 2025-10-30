from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CLASS_NAME, "screen")
        self.buttons = {
            "7": (By.XPATH, "//span[text()='7']"),
            "8": (By.XPATH, "//span[text()='8']"),
            "+": (By.XPATH, "//span[text()='+']"),
            "=": (By.XPATH, "//span[text()='=']")
        }

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, delay):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(delay)

    def click_button(self, button):
        self.driver.find_element(*self.buttons[button]).click()

    def get_result(self, timeout=52):
        result_element = self.driver.find_element(*self.screen)
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda driver: result_element.text == "15")
        return result_element.text
