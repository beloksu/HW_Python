from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    def __init__(self, driver):
        """
        Инициализирует страницу оформления заказа.

        :param driver: WebDriver для взаимодействия с браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(
            self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму данными и отправляет ее.

        :param first_name: Имя пользователя.
        :type first_name: str
        :param last_name: Фамилия пользователя.
        :type last_name: str
        :param postal_code: Почтовый индекс.
        :type postal_code: str
        :return: None
        """
        with allure.step("Заполнение формы"):
            self.wait.until(EC.visibility_of_element_located(
                (By.ID, "first-name"))).send_keys(first_name)
            self.driver.find_element(By.ID, "last-name").send_keys(last_name)
            self.driver.find_element(
                By.ID, "postal-code").send_keys(postal_code)
            self.driver.find_element(
                By.CSS_SELECTOR, "input[type='submit']").click()

    def get_total_amount(self) -> str:
        """
        Получает общую сумму заказа.

        :return: Сумма заказа.
        :rtype: str
        """
        with allure.step("Получение общей суммы заказа"):
            total_element = self.wait.until(EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")))
            return total_element.text.split()[-1]
