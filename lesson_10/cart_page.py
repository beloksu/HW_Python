from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    def __init__(self, driver):
        """
        Инициализирует страницу корзины.

        :param driver: WebDriver для взаимодействия с браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def proceed_to_checkout(self) -> None:
        """
        Переходит к оформлению заказа.

        :return: None
        """
        with allure.step("Переход к оформлению заказа"):
            self.wait.until(EC.visibility_of_element_located(
                (By.ID, "checkout"))).click()
