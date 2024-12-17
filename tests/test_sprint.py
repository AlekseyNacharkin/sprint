import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_elements_list():
    driver = webdriver.Chrome()
    driver.get("https://qa-scooter.praktikum-services.ru/order")
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='* Станция метро']").click()
    time.sleep(3)
    elements = driver.find_element(By.CSS_SELECTOR, ".select-search__select")
    wait = WebDriverWait(driver, 10)  # Устанавливаем тайм-аут 10 секунд
    elements = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".select-search__select"))
    )
    #list_items = elements.find_elements(By.CSS_SELECTOR, ".select-search__option")
    #for item in list_items:
    #    print(item.text)
    sokolniki = wait.until(EC.presence_of_element_located((By.XPATH, ".//div[@class='Order_Text__2broi' and contains(text(),'Сокольники')]/parent::button")))
    sokolniki.click()

    # Проверяем и взаимодействуем с элементом
    #print("Элемент найден:", elements)
    time.sleep(2)