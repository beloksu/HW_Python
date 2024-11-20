from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import allure


class FormPage:
    def __init__(self, driver):
        """
        Инициализирует страницу с формой.

        :param driver: WebDriver для взаимодействия с браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def open_page(self, url: str) -> None:
        """
        Открывает страницу по указанному URL.

        :param url: URL страницы.
        :type url: str
        :return: None
        """
        with allure.step(f"Открытие страницы: {url}"):
            self.driver.get(url)

    def enter_value(self, name: str, value: str) -> None:
        """
        Вводит значение в поле с указанным именем.

        :param name: Имя поля.
        :type name: str
        :param value: Значение для ввода.
        :type value: str
        :return: None
        """
        with allure.step(f"Ввод значения '{value}' в поле '{name}'"):
            for attempt in range(3):
                try:
                    field = self.wait.until(EC.presence_of_element_located(
                        (By.NAME, name)))
                    field.clear()
                    field.send_keys(value)
                    return
                except StaleElementReferenceException:
                    if attempt == 2:
                        raise Exception(
                            f"Не удалось ввести значение в поле '{name}'."
                        )

    def submit_form(self) -> None:
        """
        Нажимает кнопку отправки формы.

        :return: None
        """
        with allure.step("Отправка формы"):
            submit_button = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']")))
            submit_button.click()

    def get_field_border_color(self, field_id: str) -> str:
        """
        Получает цвет границы поля по его ID.

        :param field_id: ID поля.
        :type field_id: str
        :return: Цвет границы.
        :rtype: str
        """
        with allure.step(f"Получение цвета границы поля '{field_id}'"):
            field = self.wait.until(EC.visibility_of_element_located(
                (By.ID, field_id)))
            return field.value_of_css_property("border-color")

    def get_zip_code_border_color(self) -> str:
        """
        Получает цвет границы поля почтового индекса.

        :return: Цвет границы.
        :rtype: str
        """
        with allure.step("Получение цвета границы поля 'zip-code'"):
            zip_code_field = self.wait.until(EC.visibility_of_element_located(
                (By.ID, "zip-code")))
            return zip_code_field.value_of_css_property("border-color")
