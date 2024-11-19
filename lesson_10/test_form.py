import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_form_submission(driver):
    form_page = FormPage(driver)
    form_page.open_page(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

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

    for name, value in input_data.items():
        form_page.enter_value(name, value)

    form_page.submit_form()

    zip_code_border_color = form_page.get_zip_code_border_color()
    assert zip_code_border_color == "rgb(245, 194, 199)"

    fields_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]
    for field_name in fields_to_check:
        border_color = form_page.get_field_border_color(field_name)
        assert border_color == "rgb(186, 219, 204)"
