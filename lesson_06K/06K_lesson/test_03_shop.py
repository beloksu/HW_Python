from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.ID, "checkout"))).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.ID, "first-name"))).send_keys("ВашеИмя")
    driver.find_element(By.ID, "last-name").send_keys("ВашаФамилия")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    print("Получаем итоговую стоимость...")
    total_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")))
    total_amount = total_element.text.split()[-1]

    print(f"Итоговая сумма: {total_amount}")
    assert total_amount == "$58.29", (
        f"Ожидалось $58.29, но получено {total_amount}.")
    print("Тест пройден успешно! Итоговая сумма верна.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
