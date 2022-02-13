import pytest
from selenium import webdriver

#фикстура, которая подтягивает драйвер веб браузера .
@pytest.fixture
def driver():
    driver = webdriver.Chrome('chromedriver.exe')# путь к файлу с драйвером
    driver.maximize_window()# размер окна браузера при запуске тестов
    driver.implicitly_wait(10) # неявное ожидание , чтобы сайт загрузился
    yield driver
    driver.quit()