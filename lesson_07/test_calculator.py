import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.open_page(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calculator_page.set_delay("45")

    buttons = ["7", "+", "8", "="]
    for button in buttons:
        calculator_page.click_button(button)

    calculator_page.wait_for_result("15")
    result_text = calculator_page.get_result_text()

    assert result_text == "15", f"ОР не 15, а {result_text}!"
