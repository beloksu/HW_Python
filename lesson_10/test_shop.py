import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    """
    Фикстура для создания экземпляра веб-драйвера.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@allure.feature("Shopping Process")
@allure.title("Тест полного процесса покупки")
@allure.description(
    "Проверка авторизации, добавления товаров в корзину, "
    "оформления заказа и итоговой суммы"
    )
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    with allure.step("Авторизация пользователя"):
        login_page = LoginPage(driver)
        login_page.open_page("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        inventory_page = InventoryPage(driver)
        with allure.step("Добавление рюкзака в корзину"):
            inventory_page.add_item_to_cart("add-to-cart-sauce-labs-backpack")
        with allure.step("Добавление футболки в корзину"):
            inventory_page.add_item_to_cart(
                "add-to-cart-sauce-labs-bolt-t-shirt")
        with allure.step("Добавление комбинезона в корзину"):
            inventory_page.add_item_to_cart("add-to-cart-sauce-labs-onesie")
        inventory_page.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()

    with allure.step("Заполнение формы оформления заказа"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("ВашеИмя", "ВашаФамилия", "12345")

    with allure.step("Проверка итоговой суммы заказа"):
        total_amount = checkout_page.get_total_amount()
        assert total_amount == "$58.29", "ОР $58.29, "
        f"но получено {total_amount}."
