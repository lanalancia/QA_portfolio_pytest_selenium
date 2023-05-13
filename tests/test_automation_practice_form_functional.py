from locators import LocatorsAutomationPracticeForm
from common_methods import Methods

"""Submit info with required fields only.

Test Case: [LINK TO A TEST CASE]
1. Open the https://demoqa.com/automation-practice-form page
2. Fill the required fields only: First name, Last name, Gender, Mobile number
3. Press submit

Expected behavior: info submitted successfully"""


def test_submit_required_only(create_webdriver):
    driver = create_webdriver
    methods = Methods(driver)
    locators = LocatorsAutomationPracticeForm()

    driver.maximize_window()
    driver.get("https://demoqa.com/automation-practice-form")
    """Advertisments bypass"""
    driver.get("https://demoqa.com/automation-practice-form")
    methods.click_and_input(locators.INPUT_FIELD_FIRST_NAME, "FirstName")
    methods.click_and_input(locators.INPUT_FIELD_LAST_NAME, "LastName")
    methods.click_and_input(locators.INPUT_FIELD_PHONE_NUMBER, "0123456789")
    methods.click(locators.RADIO_GENDER_MALE)
    methods.click_with_offset(locators.BUTTON_SUBMIT, 0, -10)

    """Check if \"Thanks for submitting information\" block is present """
    assert methods.locator_is_present(locators.OBJECT_SUBMITTED_INFO), "Submit confirmation window not appears"

def test_submit_full_info(create_webdriver):
    driver = create_webdriver
    methods = Methods(driver)
    locators = LocatorsAutomationPracticeForm()

    driver.maximize_window()
    driver.get("https://demoqa.com/automation-practice-form")
    """Advertisments bypass"""
    driver.get("https://demoqa.com/automation-practice-form")

    methods.click_and_input(locators.INPUT_FIELD_FIRST_NAME, "FirstName")
    methods.click_and_input(locators.INPUT_FIELD_LAST_NAME, "LastName")
    methods.click_and_input(locators.INPUT_FIELD_PHONE_NUMBER, "0123456789")
    methods.click_and_input(locators.INPUT_FIELD_EMAIL, "test@example.com")
    methods.click(locators.RADIO_GENDER_FEMALE)
    methods.click_and_replace(locators.INPUT_FIELD_DOB, "03 May 2011")
    methods.press_enter_here()
    methods.click(locators.FLAG_HOBBY_SPORTS)
    methods.click(locators.FLAG_HOBBY_MUSIC)
    methods.click(locators.FLAG_HOBBY_READING)
    methods.click(locators.FIELD_SUBJECTS)
    methods.input_text_here("a")
    methods.press_enter_here()
    methods.click_and_input(locators.INPUT_FIELD_ADDRESS, "London, Baker street, 2")
    methods.click(locators.DROPDOWN_STATE)
    methods.click(locators.DROPDOWN_STATE_1ST)
    methods.click(locators.DROPDOWN_CITY)
    methods.click(locators.DROPDOWN_CITY_1ST)
    methods.click_with_offset(locators.BUTTON_SUBMIT, 0, -12)

    """Check if \"Thanks for submitting information\" block is present """
    assert methods.locator_is_present(locators.OBJECT_SUBMITTED_INFO), "Submit confirmation window not appears"
