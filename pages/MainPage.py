from pages.BasePage import BasePage
from config import TestData
from selenium.webdriver.common.by import By

#класс содержит локаторы

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

#Form Autentification
    FORM_AUTENTIFICATION = (By.XPATH, "//a[contains (text(), 'Form Authentication')]")
    HEAD_OF_FORM_AUTENTIFICATION = (By.XPATH, "//h2[contains (text(), 'Login Page')]")
    INPUT_FIELD_USERNAME = (By.XPATH, "//input[@id = 'username']")
    INPUT_FIELD_PASSWORD = (By.XPATH, "//input[@id = 'password']")
    BUTTON_SUBMIT = (By.XPATH, "//button[@type = 'submit']")
    HEAD_PAGE_SECURE_AREA = (By.XPATH, "//h2[contains (text(), ' Secure Area')]")

#DropDown List
    DROPDOWN_LIST = (By.XPATH, "//a[contains (text(), 'Dropdown')]")
    HEAD_OF_DROPDOWN_LIST = (By.XPATH, "//h3[contains (text(), 'Dropdown List')]")
    INPUT_SELECT_OPTION = (By.CSS_SELECTOR, "select#dropdown")
    INPUT_SELECT_OPTION_1 = (By.XPATH, "//select[@id = 'dropdown']//option[@value = '1']")

#Key Presses
    KEY_PRESSES = ((By.XPATH, "//a[contains (text(), 'Key Presses')]"))
    HEAD_OF_KEY_PRESSES = (By.XPATH, "//h3[contains (text(), 'Key Presses')]")
    INPUT_FIELD_KEY_PRESSES = (By.CSS_SELECTOR, "input#target")
    RESULT_INPUT_KEY_PRESSES = (By.CSS_SELECTOR, "p#result")

#File DownLoad
    FILE_DOWNLOAD = (By.XPATH, "//a[contains (text(), 'File Download')]")
    HEAD_OF_FILE_DOWNLOAD = (By.XPATH, "//h3[contains (text(), 'File Downloader')]")
    CHOSE_FILE_DOWNLOAD = (By.XPATH, "//a[contains (text(), 'some-file.txt')]")