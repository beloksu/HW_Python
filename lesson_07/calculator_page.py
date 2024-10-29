from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open_page(self, url):
        self.driver.get(url)

    def set_delay(self, delay_value):
        delay_input = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys(delay_value)

    def click_button(self, button_text):
        button_element = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[text()='{button_text}']"))
        )
        button_element.click()

    def wait_for_result(self, expected_text):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), expected_text)
        )

    def get_result_text(self):
        result_element = self.driver.find_element(By.CLASS_NAME, "screen")
        return result_element.text
