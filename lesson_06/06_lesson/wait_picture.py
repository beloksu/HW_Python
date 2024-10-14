from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 15)
wait.until(EC.text_to_be_present_in_element((By.ID, "text"), 'Done!'))

third_image = driver.find_element(By.CSS_SELECTOR, "img:nth-of-type(3)")
src_value = third_image.get_attribute("src")

print(f"Значение атрибута src у 3-й картинки: {src_value}")

driver.quit()
