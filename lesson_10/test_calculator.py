from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    def __init__(self, driver):
        """
        Инициализирует страницу входа.

        :param driver: WebDriver для взаимодействия с браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self, url: str) -> None:
        """
        Открывает страницу по указанному URL.

        :param url: URL страницы.
        :type url: str
        :return: None
        """
        with allure.step(f"Открытие страницы: {url}"):
            self.driver.get(url)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию.

        :param username: Имя пользователя.
        :type username: str
        :param password: Пароль.
        :type password: str
        :return: None
        """
        with allure.step("Ввод учетных данных и выполнение входа"):
            self.wait.until(EC.visibility_of_element_located(
                (By.ID, "user-name"))).send_keys(username)
            self.driver.find_element(By.ID, "password").send_keys(password)
            self.driver.find_element(
                By.CSS_SELECTOR, "input[type='submit']").click()
