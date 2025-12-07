import allure
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.feature("Shopping Cart")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест оформления заказа и проверки итоговой суммы")
@allure.description("""
Полный сценарий покупки в интернет-магазине:
1. Авторизация стандартного пользователя
2. Добавление трех товаров в корзину
3. Переход в корзину и оформление заказа
4. Заполнение информации о покупателе
5. Проверка итоговой суммы заказа
""")
def test_shopping_cart_total():
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        with allure.step("Открытие страницы авторизации"):
            login_page.open()

        with allure.step("Авторизация пользователя standard_user"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавление товаров в корзину"):
            main_page.add_item_to_cart("backpack")
            main_page.add_item_to_cart("bolt_t_shirt")
            main_page.add_item_to_cart("onesie")

        with allure.step("Переход в корзину"):
            main_page.go_to_cart()

        with allure.step("Начало оформления заказа"):
            cart_page.checkout()

        with allure.step("Заполнение информации о покупателе"):
            checkout_page.fill_checkout_info("Иван", "Петров", "123456")

        with allure.step("Получение итоговой суммы"):
            total_text = checkout_page.get_total_amount()

        with allure.step("Проверка итоговой суммы $58.29"):
            assert total_text == "Total: $58.29", f"Ожидалась сумма $58.29, но получена {total_text}"

        allure.attach(f"Итоговая сумма заказа: {total_text}", name="Total Amount")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_shopping_cart_total()