import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage


@pytest.fixture
def driver():
    """
    Фикстура для создания экземпляра веб-драйвера.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@allure.feature("Form Submission")
@allure.title("Тест отправки формы")
@allure.description("Проверка заполнения полей и цвета границ после отправки")
@allure.severity(allure.severity_level.NORMAL)
def test_form_submission(driver):
    with allure.step("Инициализация страницы формы"):
        form_page = FormPage(driver)

    with allure.step("Открытие страницы формы"):
        form_page.open_page(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    input_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    with allure.step("Заполнение полей формы"):
        for name, value in input_data.items():
            with allure.step(f"Ввод значения '{value}' в поле '{name}'"):
                form_page.enter_value(name, value)

    with allure.step("Отправка формы"):
        form_page.submit_form()

    with allure.step("Проверка цвета границы поля ZIP-кода"):
        zip_code_border_color = form_page.get_zip_code_border_color()
        assert zip_code_border_color == "rgb(245, 194, 199)", (
            "Ожидаемый цвет 'rgb(245, 194, 199)', "
            f"но получен {zip_code_border_color}"
        )

    fields_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    with allure.step("Проверка цвета границ остальных полей"):
        for field_name in fields_to_check:
            with allure.step(f"Проверка цвета границы поля '{field_name}'"):
                border_color = form_page.get_field_border_color(field_name)
                assert border_color == "rgb(186, 219, 204)", (
                    "Ожидаемый цвет 'rgb(186, 219, 204)', "
                    f"но получен {border_color}"
                )
