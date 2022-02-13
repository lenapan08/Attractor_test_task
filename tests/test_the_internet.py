from pages.MainPage import MainPage
from config import TestData
import requests

#для запуска тестов в терминале набираем pytest tests

#авто-тест на теск-кейс №1
def test_form_autentification(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.FORM_AUTENTIFICATION)
    # title = main_page.is_visible(MainPage.HEAD_OF_FORM_AUTENTIFICATION)
    #assert title == True #проверка - попали на страницу форма аутентификации
    main_page.do_send_keys(MainPage.INPUT_FIELD_USERNAME, TestData.USERNAME)
    main_page.do_send_keys(MainPage.INPUT_FIELD_PASSWORD, TestData.PASSWORD)
    main_page.find_click(MainPage.BUTTON_SUBMIT)
    title = main_page.get_text_of_element(MainPage.HEAD_PAGE_SECURE_AREA)
    assert title == TestData.SECURE_AREA

#авто-тест на теск-кейс №2
def test_drop_list(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.DROPDOWN_LIST)
    #title = main_page.is_visible(MainPage.HEAD_OF_DROPDOWN_LIST)
    #assert title == True#проверка - попали на страницу Dropdownlist
    main_page.find_click(MainPage.INPUT_SELECT_OPTION)
    main_page.find_click(MainPage.INPUT_SELECT_OPTION_1)
    select = main_page.is_visible(MainPage.INPUT_SELECT_OPTION_1)
    assert select == True

#авто-тест на теск-кейс №3
def test_key_presses(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.KEY_PRESSES)
    # title = main_page.is_visible(MainPage.HEAD_OF_KEY_PRESSES)
    # assert title == True #проверка - попали на страницу Key Presses
    main_page.find_click(MainPage.INPUT_FIELD_KEY_PRESSES)
    main_page.do_send_keys(MainPage.INPUT_FIELD_KEY_PRESSES, TestData.KEY_PRESSES_INPUT_DATA)
    result = main_page.get_text_of_element(MainPage.RESULT_INPUT_KEY_PRESSES)
    assert result == TestData.RESULT_INPUT_DATA

#авто-тест на теск-кейс №4
def test_file_download(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.FILE_DOWNLOAD)
    # title = main_page.is_visible(MainPage.HEAD_OF_FILE_DOWNLOAD)
    # assert title == True #проверка - попали на страницу DownLoadFile
    requests.get(TestData.BASE_URL + TestData.HREF_FILE)
    my_file = open('details.txt', 'r', encoding='utf8')
    # for line in my_file:
    #     if 'ansi' in line:
    #         print('OK!')
    assert TestData.PART_IN_FILE in my_file




