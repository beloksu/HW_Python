import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_shop(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart("add-to-cart-sauce-labs-backpack")
    inventory_page.add_item_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inventory_page.add_item_to_cart("add-to-cart-sauce-labs-onesie")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("ВашеИмя", "ВашаФамилия", "12345")
    total_amount = checkout_page.get_total_amount()

    assert total_amount == "$58.29", f"ОР $58.29, но получено {total_amount}."
