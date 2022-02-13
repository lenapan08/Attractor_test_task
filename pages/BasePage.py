from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  requests
from config import TestData

#класс содержит все методы, которые используются для написания тестов
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    #найти элемент и кликнуть по нему
    def find_click(self, by_locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator)).click()

    # Проверить видимость элемента
    def is_visible(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    #Ввести данные в строку
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    #Получить  атрибут текст элемента
    def get_text_of_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text


