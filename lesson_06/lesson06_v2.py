from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("http://uitestingplayground.com/textinput")

    element = driver.find_element(By.ID, "newButtonName")

    element.clear()

    element.send_keys("SkyPro")

    driver.find_element(By.ID, "updatingButton").click()

    button = driver.find_element(By.ID, "updatingButton")

    button_text = button.text

    print(button_text)

    sleep(2)
finally:
    driver.quit()
