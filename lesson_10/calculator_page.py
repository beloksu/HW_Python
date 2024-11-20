from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    def __init__(self, driver):
        """
        Инициализирует страницу калькулятора.

        :param driver: WebDriver для взаимодействия с браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open_page(self, url: str) -> None:
        """
        Открывает страницу по указанному URL.

        :param url: URL страницы.
        :type url: str
        :return: None
        """
        with allure.step(f"Открытие страницы: {url}"):
            self.driver.get(url)

    def set_delay(self, delay_value: str) -> None:
        """
        Устанавливает задержку на странице.

        :param delay_value: Значение задержки.
        :type delay_value: str
        :return: None
        """
        with allure.step(f"Установка задержки: {delay_value}"):
            delay_input = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay"))
            )
            delay_input.clear()
            delay_input.send_keys(delay_value)

    def click_button(self, button_text: str) -> None:
        """
        Нажимает кнопку с указанным текстом.

        :param button_text: Текст кнопки.
        :type button_text: str
        :return: None
        """
        with allure.step(f"Нажатие кнопки: {button_text}"):
            button_element = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//span[text()='{button_text}']"))
            )
            button_element.click()

    def wait_for_result(self, expected_text: str) -> None:
        """
        Ожидает появления ожидаемого текста на экране.

        :param expected_text: Ожидаемый текст.
        :type expected_text: str
        :return: None
        """
        with allure.step(f"Ожидание результата: {expected_text}"):
            self.wait.until(
                EC.text_to_be_present_in_element(
                    (By.CLASS_NAME, "screen"), expected_text)
            )

    def get_result_text(self) -> str:
        """
        Получает текст результата.

        :return: Текст результата.
        :rtype: str
        """
        with allure.step("Получение текста результата"):
            result_element = self.driver.find_element(By.CLASS_NAME, "screen")
            return result_element.text
