from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")

blue_button = driver.find_element(
    By.XPATH,
    "//button[contains(text(), 'Button with Dynamic ID')]"
)
