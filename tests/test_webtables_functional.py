import pytest
import sys

sys.path.append('../QA_portfolio_pytest_selenium')

from locators import LocatorsWebtables
from common_methods import Methods

"""Functional testing for https://demoqa.com/webtables page."""

@pytest.fixture
def webtables_prerequisites():
    return ["auto_first", "auto_last", "testmail@test.com", "99", "9999", "IT"]


"""Test Case: [LINK TO A TEST CASE]
1. Open the https://demoqa.com/webtables page
2. Add a new row with some data
3. Check the created row

Expected behavior: row deleted successfully"""


def test_webtables_create_entry(create_webdriver, webtables_prerequisites):
    driver = create_webdriver
    driver.maximize_window()
    driver.get("https://demoqa.com/webtables")

    methods = Methods(driver)
    locators = LocatorsWebtables()
    testing_data = webtables_prerequisites
    methods.click(locators.BUTTON_ADD)
    locators.set_metadata(testing_data[0])
    methods.click_and_input(locators.INPUT_FIELD_FIRST_NAME, testing_data[0])
    methods.click_and_input(locators.INPUT_FIELD_LAST_NAME, testing_data[1])
    methods.click_and_input(locators.INPUT_FIELD_EMAIL, testing_data[2])
    methods.click_and_input(locators.INPUT_FIELD_AGE, testing_data[3])
    methods.click_and_input(locators.INPUT_FIELD_SALARY, testing_data[4])
    methods.click_and_input(locators.INPUT_FIELD_DEPARTMENT, testing_data[5])
    methods.click(locators.BUTTON_SUBMIT)

    """An array is collecting validations for each field. The values are bool."""
    result: list[bool] = [methods.compare_element_text_with(locators.TABLE_FIELD_FIRST_NAME, testing_data[0]),
                          methods.compare_element_text_with(locators.TABLE_FIELD_LAST_NAME, testing_data[1]),
                          methods.compare_element_text_with(locators.TABLE_FIELD_EMAIL, testing_data[2]),
                          methods.compare_element_text_with(locators.TABLE_FIELD_AGE, testing_data[3]),
                          methods.compare_element_text_with(locators.TABLE_FIELD_SALARY, testing_data[4]),
                          methods.compare_element_text_with(locators.TABLE_FIELD_DEPARTMENT, testing_data[5])]

    """Single assertion for entire row. Assert field equals to testing_data"""
    assert all(result), "Some value is different from expected"
    driver.close()


"""Test Case: [LINK TO A TEST CASE]
1. Open the https://demoqa.com/webtables page
2. Edit any entry
3. Save changes
4. Check the created row

Expected behavior: changes are applied to a chosen row."""


@pytest.mark.parametrize("first_name", [
    "Cierra",
    "Kierra",
    "Alden"
])
def test_edit_entry(create_webdriver, first_name, webtables_prerequisites):  # Задание 2. Редактирование существующей записи
    driver = create_webdriver
    driver.maximize_window()
    driver.get("https://demoqa.com/webtables")

    methods = Methods(driver)
    locators = LocatorsWebtables()
    testing_data = webtables_prerequisites

    locators.set_metadata(first_name)
    methods.click(locators.BUTTON_EDIT)
    methods.click_and_replace(locators.INPUT_FIELD_FIRST_NAME, testing_data[0])
    methods.click_and_replace(locators.INPUT_FIELD_LAST_NAME, testing_data[1])
    methods.click_and_replace(locators.INPUT_FIELD_EMAIL, testing_data[2])
    methods.click_and_replace(locators.INPUT_FIELD_AGE, testing_data[3])
    methods.click_and_replace(locators.INPUT_FIELD_SALARY, testing_data[4])
    methods.click_and_replace(locators.INPUT_FIELD_DEPARTMENT, testing_data[5])
    methods.click(locators.BUTTON_SUBMIT)

    """Due to a row being selected by a Name field, I change the metadata to a testing_data[0]. This will make test 
    to search for a row with a testing_data[0] value in a name field."""
    locators.set_metadata(testing_data[0])

    """An array is collecting validations for each field. The values are bool."""
    result: list[bool] = [methods.compare_element_text_with(locators.TABLE_FIELD_FIRST_NAME, testing_data[0]),
                          methods.compare_element_text_with(locators.TABLE_FIELD_LAST_NAME, testing_data[1]),
                          methods.compare_element_text_with(locators.TABLE_FIELD_EMAIL, testing_data[2]),
                          methods.compare_element_text_with(locators.TABLE_FIELD_AGE, testing_data[3]),
                          methods.compare_element_text_with(locators.TABLE_FIELD_SALARY, testing_data[4]),
                          methods.compare_element_text_with(locators.TABLE_FIELD_DEPARTMENT, testing_data[5])]

    """Single assertion for entire row. Assert field equals to testing_data"""
    assert all(result), "Some value is not edited successfully"
    driver.close()


"""Test Case: [LINK TO A TEST CASE]
1. Open the https://demoqa.com/webtables page
2. Delete any row

Expected behavior: a deleted row is not present in a table."""


@pytest.mark.parametrize("first_name", [
    "Alden",
    "Kierra"
])
def test_delete_entry(create_webdriver, first_name):
    driver = create_webdriver
    driver.maximize_window()
    driver.get("https://demoqa.com/webtables")

    methods = Methods(driver)
    locators = LocatorsWebtables()

    locators.set_metadata(first_name)
    methods.click(locators.BUTTON_DELETE)
    assert not methods.locator_is_present(locators.INPUT_FIELD_FIRST_NAME), "Entry is still exists after deletion"
    driver.close()
