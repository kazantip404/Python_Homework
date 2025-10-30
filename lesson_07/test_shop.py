from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shopping_cart_total():
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        main_page.add_item_to_cart("backpack")
        main_page.add_item_to_cart("bolt_t_shirt")
        main_page.add_item_to_cart("onesie")
        main_page.go_to_cart()

        cart_page.checkout()

        checkout_page.fill_checkout_info("Иван", "Петров", "123456")
        total_text = checkout_page.get_total_amount()

        assert total_text == "Total: $58.29"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_shopping_cart_total()
