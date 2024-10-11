from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)

driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.XPATH, "//input[@type='number']")

input_field.send_keys("1000")

input_field.clear()

input_field.send_keys("999")

driver.quit()
