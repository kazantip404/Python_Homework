from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")
        self.items = {
            "backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "bolt_t_shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "onesie": (By.ID, "add-to-cart-sauce-labs-onesie")
        }

    def add_item_to_cart(self, item_name):
        self.driver.find_element(*self.items[item_name]).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
