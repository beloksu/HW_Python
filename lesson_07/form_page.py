from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def open_page(self, url):
        self.driver.get(url)

    def enter_value(self, name, value):
        for attempt in range(3):
            try:
                field = self.wait.until(
                    EC.presence_of_element_located((By.NAME, name)))
                field.clear()
                field.send_keys(value)
                return
            except StaleElementReferenceException:
                if attempt == 2:
                    raise Exception(
                        f"Не удалось ввести значение в поле '{name}'.")

    def submit_form(self):
        submit_button = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()

    def get_field_border_color(self, field_id):
        field = self.wait.until(
            EC.visibility_of_element_located((By.ID, field_id)))
        return field.value_of_css_property("border-color")

    def get_zip_code_border_color(self):
        zip_code_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "zip-code")))
        return zip_code_field.value_of_css_property("border-color")
