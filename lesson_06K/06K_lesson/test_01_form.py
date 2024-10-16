from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException
)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 30)

    def enter_value(name, value):
        for attempt in range(3):
            try:
                print(f"Ожидание поля '{name}'...")
                field = wait.until(
                    EC.presence_of_element_located((By.NAME, name))
                )
                field.clear()
                field.send_keys(value)
                print(f"Введено значение '{value}' в поле '{name}'.")
                return
            except StaleElementReferenceException:
                print(
                    f"Попытка {attempt + 1}: поле '{name}' недоступно."
                    )
                if attempt == 2:
                    raise Exception(
                        f"Не удалось ввести значение в поле '{name}' после "
                        f"нескольких попыток."
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

    for name, value in input_data.items():
        enter_value(name, value)

    print("Ожидание кнопки Submit...")
    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()
    print("Кнопка Submit нажата.")

    print("Ожидание поля Zip code...")
    zip_code_field = wait.until(
        EC.visibility_of_element_located((By.NAME, "zip-code"))
    )
    zip_code_border_color = zip_code_field.value_of_css_property(
        "border-color")
    assert zip_code_border_color == "rgb(255, 0, 0)", (
        "Поле Zip code не красное!"
    )

    fields_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field_name in fields_to_check:
        print(f"Ожидание поля {field_name}...")
        field = wait.until(
            EC.visibility_of_element_located((By.NAME, field_name))
        )
        border_color = field.value_of_css_property("border-color")
        assert border_color == "rgb(0, 128, 0)", (
            f"Поле {field_name} не зеленое!"
        )

    print("Все проверки пройдены успешно.")

except TimeoutException as e:
    print(f"Произошла ошибка: ожидание элемента истекло: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    driver.quit()
