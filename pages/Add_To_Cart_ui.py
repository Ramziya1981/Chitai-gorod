from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.description("Тестирование добавления товара в корзину на сайте Читай-город.")
class AddToCart:
  
    # ИНИЦИАЛИЗАЦИЯ
    def __init__(self, book_title: str):
        """         Создает объект для добавления книги в корзину.

                    :param book_title: Название книги для добавления в корзину.
        """
        self.book_title = book_title

    # ПОИСК КНИГИ ПО НАЗВАНИЮ
    def add_to_card(self, driver: webdriver.Chrome) -> dict:
        """         Ищет книгу по названию и добавляет её в корзину.

                    :param driver: Экземпляр драйвера Selenium.
                    :param book_title: Название книги для поиска.
                    :return: Словарь с результатами поиска (в данном методе возвращает None).
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