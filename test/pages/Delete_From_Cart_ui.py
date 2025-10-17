from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.description("Тестирование удаления товара из корзины на сайте Читай-город.")
class DeleteFromCart:
    """Класс для удаления товара из корзины на сайте Читай-город."""

    def __init__(self, book_title: str):
        """
        Инициализация класса DeleteFromCart.
        
        :param book_title: Название книги, которую нужно удалить из корзины.
        """
        self.book_title = book_title

    @allure.step("Поиск книги по названию и удаление из корзины")
    def delete_from_cart(self, driver: webdriver.Chrome) -> None:
        """
        Поиск книги по названию, добавление в корзину и удаление из нее.

        :param driver: Экземпляр драйвера Selenium (в данном случае Chrome).
        :raises Exception: Возникает, если не удается найти элементы на странице.
        """
    
        # Ввод названия книги в строку поиска
        search_input = driver.find_element(By.NAME, "search")
        search_input.send_keys(self.book_title)
        
        # Клик по кнопке поиска
        search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Найти']")))
        search_button.click()

        #Клик по кнопке "Купить"
        parent_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
            By.CLASS_NAME,
            "product-card__content")))
        child_elements = parent_element.find_elements(By.TAG_NAME, "button")
        first_element = child_elements[0]
        print(first_element.tag_name + " " + first_element.accessible_name)
        driver.execute_script("arguments[0].click();", first_element)

        
        # Открытие корзины
        cart_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Корзина']")))
        driver.execute_script("arguments[0].click();", cart_icon)

            # Клик по кнопке "Очистить корзину"

        delete_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-page__clear-cart-title")))
        driver.execute_script("arguments[0].click();", delete_button)