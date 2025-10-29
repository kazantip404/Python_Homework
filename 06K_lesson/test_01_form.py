from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for name, value in fields.items():
        field = driver.find_element(By.NAME, name)
        field.clear()
        if value:
            field.send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(EC.url_contains("data-types-submitted.html"))

    page_text = driver.find_element(By.TAG_NAME, "body").text

    assert "Zip code\nN/A" in page_text, "Zip code должен быть N/A"

    checks = {
        "First name\nИван",
        "Last name\nПетров",
        "Address\nЛенина, 55-3",
        "E-mail\ntest@skypro.com",
        "Phone number\n+7985899998787",
        "City\nМосква",
        "Country\nРоссия",
        "Job position\nQA",
        "Company\nSkyPro"
    }

    for check in checks:
        assert check in page_text, f"Не найдено: {check}"

    driver.quit()


if __name__ == "__main__":
    test_form_validation()
