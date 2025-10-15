from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    blue_button.click()
    time.sleep(3)
except Exception as e:
    print(f"Произошла ошибка: {e}")
