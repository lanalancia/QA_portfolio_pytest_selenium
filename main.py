from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

from locators import LocatorsAutomationPracticeForm, LocatorsWebtables
from common_methods import Methods, MultiAssertHandler


@pytest.fixture
def create_webdriver():
    return webdriver.Chrome(service=Service(r"chromedriver.exe"))


def test_create_entry(create_webdriver):  # Задание 2. Создание и проверка созданной записи
    driver = create_webdriver
    driver.maximize_window()
    driver.get("https://demoqa.com/webtables")

    methods = Methods(driver)
    locators = LocatorsWebtables()
    testing_data = ["auto_first", "auto_last", "testmail@test.com", "99", "9999", "IT"]
    methods.click(locators.BUTTON_ADD)
    # Объявляю что в рамках этого теста будет произведён поиск строки с именем auto_first
    locators.set_metadata(testing_data[0])
    methods.click_and_input(locators.INPUT_FIELD_FIRST_NAME, testing_data[0])
    methods.click_and_input(locators.INPUT_FIELD_LAST_NAME, testing_data[1])
    methods.click_and_input(locators.INPUT_FIELD_EMAIL, testing_data[2])
    methods.click_and_input(locators.INPUT_FIELD_AGE, testing_data[3])
    methods.click_and_input(locators.INPUT_FIELD_SALARY, testing_data[4])
    methods.click_and_input(locators.INPUT_FIELD_DEPARTMENT, testing_data[5])
    methods.click(locators.BUTTON_SUBMIT)

    # Каждое значение в таблице сравнивается с тем, которое было внесено
    result = [methods.compare_element_text_with(locators.TABLE_FIELD_FIRST_NAME, testing_data[0]),
              methods.compare_element_text_with(locators.TABLE_FIELD_LAST_NAME, testing_data[1]),
              methods.compare_element_text_with(locators.TABLE_FIELD_EMAIL, testing_data[2]),
              methods.compare_element_text_with(locators.TABLE_FIELD_AGE, testing_data[3]),
              methods.compare_element_text_with(locators.TABLE_FIELD_SALARY, testing_data[4]),
              methods.compare_element_text_with(locators.TABLE_FIELD_DEPARTMENT, testing_data[5])]
    assert all(result), "Some value is different from expected"
    driver.close()


@pytest.mark.parametrize("first_name", [
    "Cierra",
    "Kierra",
    "Alden"
])
def test_edit_entry(create_webdriver, first_name):  # Задание 2. Редактирование существующей записи
    driver = create_webdriver
    driver.maximize_window()
    driver.get("https://demoqa.com/webtables")

    methods = Methods(driver)
    locators = LocatorsWebtables()
    testing_data = ["auto_first", "auto_last", "testmail@test.com", "99", "9999", "IT"]

    # Объявляю что в рамках этого теста будет произведён поиск строки с конкретным именем
    locators.set_metadata(first_name)
    methods.click(locators.BUTTON_EDIT)
    methods.click_and_replace(locators.INPUT_FIELD_FIRST_NAME, testing_data[0])
    methods.click_and_replace(locators.INPUT_FIELD_LAST_NAME, testing_data[1])
    methods.click_and_replace(locators.INPUT_FIELD_EMAIL, testing_data[2])
    methods.click_and_replace(locators.INPUT_FIELD_AGE, testing_data[3])
    methods.click_and_replace(locators.INPUT_FIELD_SALARY, testing_data[4])
    methods.click_and_replace(locators.INPUT_FIELD_DEPARTMENT, testing_data[5])
    methods.click(locators.BUTTON_SUBMIT)

    # Так как тестируемый в рамках задачи элемент был переименован на auto_first, я меняю имя, по которому ищется строка
    locators.set_metadata(testing_data[0])

    result = [methods.compare_element_text_with(locators.TABLE_FIELD_FIRST_NAME, testing_data[0]),
              methods.compare_element_text_with(locators.TABLE_FIELD_LAST_NAME, testing_data[1]),
              methods.compare_element_text_with(locators.TABLE_FIELD_EMAIL, testing_data[2]),
              methods.compare_element_text_with(locators.TABLE_FIELD_AGE, testing_data[3]),
              methods.compare_element_text_with(locators.TABLE_FIELD_SALARY, testing_data[4]),
              methods.compare_element_text_with(locators.TABLE_FIELD_DEPARTMENT, testing_data[5])]
    assert all(result), "Some value is not edited successfully"
    driver.close()


@pytest.mark.parametrize("first_name", [
    "Alden",
    "Kierra"
])
def test_delete_entry(create_webdriver, first_name): # Задание 2: удаление записи
    driver = create_webdriver
    driver.maximize_window()
    driver.get("https://demoqa.com/webtables")

    methods = Methods(driver)
    locators = LocatorsWebtables()

    # Объявляю что в рамках этого теста будет произведён поиск строки с конкретным именем из parametrize
    locators.set_metadata(first_name)
    methods.click(locators.BUTTON_DELETE)
    assert not methods.locator_is_present(locators.INPUT_FIELD_FIRST_NAME), "Entry is still exists after deletion"
    driver.close()


# Так как в задании не было конкретезировано, какие именно элементы ключевые - я проверил все элементы,
# в которые можно вводить информацию, также я проверил наличие скрытых элементов (календарь и т.д.) и проверил что
# данные успешно загружаются
def test_elements_assertion(create_webdriver):  # задание 1
    driver = create_webdriver
    driver.maximize_window()
    driver.get("https://demoqa.com/automation-practice-form")
    methods = Methods(driver)
    locators = LocatorsAutomationPracticeForm()
    mah = MultiAssertHandler()

    # валидация наличия полей для ввода
    mah.assert_single(methods.locator_is_present(locators.INPUT_FIELD_FIRST_NAME),
                      "First Name input field is not found")
    mah.assert_single(methods.locator_is_present(locators.INPUT_FIELD_LAST_NAME), "Last Name input field is not found")
    mah.assert_single(methods.locator_is_present(locators.INPUT_FIELD_EMAIL), "Email input field is not found")
    mah.assert_single(methods.locator_is_present(locators.INPUT_FIELD_PHONE_NUMBER),
                      "Phone Number input field is not found")
    mah.assert_single(methods.locator_is_present(locators.RADIO_GENDER_MALE), "Male gender button is not found")
    mah.assert_single(methods.locator_is_present(locators.RADIO_GENDER_FEMALE), "Female gender button is not found")
    mah.assert_single(methods.locator_is_present(locators.RADIO_GENDER_OTHER), "Other gender button is not found")
    mah.assert_single(methods.locator_is_present(locators.FLAG_HOBBY_SPORTS), "Sports hobby flag is not found")
    mah.assert_single(methods.locator_is_present(locators.FLAG_HOBBY_READING), "Reading hobby flag is not found")
    mah.assert_single(methods.locator_is_present(locators.FLAG_HOBBY_MUSIC), "Music hobby flag is not found")
    mah.assert_single(methods.locator_is_present(locators.INPUT_FIELD_DOB), "Date of Birth input field is not found")
    mah.assert_single(methods.locator_is_present(locators.FIELD_SUBJECTS), "Subjects field is not found")
    mah.assert_single(methods.locator_is_present(locators.BUTTON_ATTACH_PICTURE), "Picture attach button is not found")
    mah.assert_single(methods.locator_is_present(locators.INPUT_FIELD_ADDRESS), "Address input field is not found")
    mah.assert_single(methods.locator_is_present(locators.DROPDOWN_STATE), "State dropdown button is not found")
    mah.assert_single(methods.locator_is_present(locators.DROPDOWN_CITY), "City dropdown button is not found")
    mah.assert_single(methods.locator_is_present(locators.BUTTON_SUBMIT), "Submit button is not found")

    # Заполнение минимальных данных для создания записи. Также в процессе создания записи проверяются скрытые
    # элементы (календарь, выпадающий список штатов и т.д.)
    methods.click_and_input(locators.INPUT_FIELD_FIRST_NAME, "FirstName")
    methods.click_and_input(locators.INPUT_FIELD_LAST_NAME, "LastName")
    methods.click(locators.RADIO_GENDER_MALE)
    methods.click_and_input(locators.INPUT_FIELD_PHONE_NUMBER, "0123456789")
    methods.click(locators.INPUT_FIELD_DOB)
    mah.assert_single(methods.locator_is_present(locators.OBJECT_DATEPICKER), "Calendar is not found")
    # methods.replace_here("01 May 2011")
    methods.click(locators.FIELD_SUBJECTS)
    # Ввод значения "a" потому что без ввода текста меню не появляется
    methods.input_text_here("a")
    mah.assert_single(methods.locator_is_present(locators.DROPDOWN_SUBJECT_LIST), "Subjects list is not found")
    # Первый элемент в списке выбирается нажатием на Enter
    methods.press_enter_here()
    # Проверка наличия элемента автозаполнения
    mah.assert_single(methods.locator_is_present(locators.SUBJECT_ELEMENT_1ST), "Autocomplete element is not found")
    methods.click(locators.DROPDOWN_STATE)
    mah.assert_single(methods.locator_is_present(locators.DROPDOWN_STATE_LIST), "State list is not found")
    # Первый элемент в списке выбирается нажатием на элемент
    methods.click(locators.DROPDOWN_STATE_1ST)
    methods.click(locators.DROPDOWN_CITY)
    mah.assert_single(methods.locator_is_present(locators.DROPDOWN_CITY_LIST), "City list is not found")
    # Первый элемент в списке выбирается нажатием на элемент
    methods.click(locators.DROPDOWN_CITY_1ST)
    # Создаётся запись с некими данными чтобы проверить наличие окна "запись успешно создана"
    methods.click_with_offset(locators.BUTTON_SUBMIT, 0, -12)
    mah.assert_single(methods.locator_is_present(locators.OBJECT_SUBMITTED_INFO),
                      "Submit confirmation window is not found")
    mah.assert_single(methods.locator_is_present(locators.BUTTON_CLOSE), "Close button is not found")

    # Проверка всех значений одним assert
    assert mah.is_successful(), mah.retrieve_errors()
    driver.close()
