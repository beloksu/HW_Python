from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

try:
    driver.get("http://uitestingplayground.com/textinput")

    input_field = driver.find_element(By.CSS_SELECTOR, "input#newButtonName")
    input_field.send_keys("SkyPro")

    button = driver.find_element(By.CSS_SELECTOR, "button#updatingButton")
    button.click()

    button_text = button.text
    print(f"Текст кнопки: {button_text}")

finally:
    driver.quit()
