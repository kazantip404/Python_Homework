from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_slow_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 52)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    delay_field = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_field.clear()
    delay_field.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    result_element = driver.find_element(By.CLASS_NAME, "screen")
    wait.until(lambda driver: result_element.text == "15")

    assert result_element.text == "15"

    driver.quit()


if __name__ == "__main__":
    test_slow_calculator()
