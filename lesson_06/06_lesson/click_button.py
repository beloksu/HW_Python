from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

try:
    driver.get("http://uitestingplayground.com/ajax")

    button = driver.find_element(By.CSS_SELECTOR, "button#ajaxButton")
    button.click()

    wait = WebDriverWait(driver, 20)
    green_box = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div#content p.bg-success"))
    )

    text = green_box.text
    print(f"Текст из плашки: {text}")

finally:
    driver.quit()
