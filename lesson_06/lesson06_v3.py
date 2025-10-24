from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    # Ждем конкретную картинку с id="award"
    award_image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "award"))
    )

    # Получаем src атрибут
    src_value = award_image.get_attribute("src")
    print(src_value)

finally:
    driver.quit()
