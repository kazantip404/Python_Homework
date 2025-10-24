from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    # 10 сек. ожидания для загрузки всех картинок
    time.sleep(10)

    # Получаем все картинки с тегом img
    images = driver.find_elements(By.TAG_NAME, "img")

    # атрибут src
    src_value = images[3].get_attribute("src")

    print(src_value)

finally:
    driver.quit()
