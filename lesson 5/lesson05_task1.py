from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as driver:
    driver.get("http://uitestingplayground.com/classattr")

    # Используем CSS_SELECTOR для поиска элемента с классами btn и class3
    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    blue_button.click()

    print("Успешно! Кликнули на синюю кнопку через CSS_SELECTOR")
    time.sleep(5)
