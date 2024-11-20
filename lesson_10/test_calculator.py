import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    """
    Фикстура для создания экземпляра веб-драйвера.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@allure.feature("Calculator Feature")
@allure.title("Тест работы калькулятора")
@allure.description("Проверка корректности вычисления 7 + 8 = 15 с задержкой")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    with allure.step("Инициализация страницы калькулятора"):
        calculator_page = CalculatorPage(driver)

    with allure.step("Открытие страницы калькулятора"):
        calculator_page.open_page(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    with allure.step("Установка задержки на 45 секунд"):
        calculator_page.set_delay("45")

    with allure.step("Нажатие кнопок 7, +, 8, ="):
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            calculator_page.click_button(button)

    with allure.step("Ожидание результата 15"):
        calculator_page.wait_for_result("15")

    with allure.step("Получение текста результата"):
        result_text = calculator_page.get_result_text()

    with allure.step("Проверка результата"):
        assert result_text == "15", f"ОР не 15, а {result_text}!"
