import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@allure.feature("Slow Calculator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест медленного калькулятора с задержкой 45 секунд")
@allure.description("""
Проверка работы калькулятора с установленной задержкой вычислений:
1. Открытие калькулятора
2. Установка задержки 45 секунд
3. Выполнение операции 7 + 8
4. Ожидание результата 15
""")
def test_slow_calculator():
    driver = webdriver.Chrome()
    calculator_page = CalculatorPage(driver)

    try:
        with allure.step("Открытие страницы калькулятора"):
            calculator_page.open()

        with allure.step("Установка задержки вычислений 45 секунд"):
            calculator_page.set_delay("45")

        with allure.step("Выполнение операции 7 + 8"):
            calculator_page.click_button("7")
            calculator_page.click_button("+")
            calculator_page.click_button("8")
            calculator_page.click_button("=")

        with allure.step("Получение и проверка результата"):
            result = calculator_page.get_result()

        with allure.step("Проверка что результат равен 15"):
            assert result == "15", f"Ожидался результат 15, но получен {result}"

        allure.attach(f"Результат вычислений: {result}", name="Calculation Result")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()