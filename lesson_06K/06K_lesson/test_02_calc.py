from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

wait = WebDriverWait(driver, 45)

delay_input = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#delay")))

delay_input.clear()
delay_input.send_keys("45")

buttons = ["7", "+", "8", "="]

for button in buttons:

    button_visible = wait.until(EC.presence_of_element_located(
        (By.XPATH, f"//span[text()='{button}']")))

    button_element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//span[text()='{button}']")))

    button_element.click()

wait = WebDriverWait(driver, 50)

result_element = wait.until(EC.text_to_be_present_in_element(
    (By.CLASS_NAME, "screen"), "15"))

result_text = driver.find_element(By.CLASS_NAME, "screen").text
assert result_text == "15", (
    f"Ожидаемый результат не равен 15, а получен {result_text}!")

print("Тест прошел успешно! Результат равен 15.")

driver.quit()
