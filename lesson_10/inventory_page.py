from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class InventoryPage:
    def __init__(self, driver):
        """
        Инициализирует страницу с товарами.

        :param driver: WebDriver для взаимодействия с браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_item_to_cart(self, item_id: str) -> None:
        """
        Добавляет товар в корзину по его ID.

        :param item_id: ID товара.
        :type item_id: str
        :return: None
        """
        with allure.step(f"Добавление товара с ID '{item_id}' в корзину"):
            self.wait.until(EC.visibility_of_element_located(
                (By.ID, item_id))).click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину.

        :return: None
        """
        with allure.step("Переход в корзину"):
            self.driver.find_element(
                By.CLASS_NAME, "shopping_cart_link").click()
