from selenium.webdriver.common.by import By


"""This file contains locators for all project. Locators for each page contained in a specific class."""


class LocatorsAutomationPracticeForm:

    """Locators for https://demoqa.com/automation-practice-form"""

    INPUT_FIELD_FIRST_NAME = (By.XPATH, '//div/input[@placeholder="First Name"]')
    INPUT_FIELD_LAST_NAME = (By.XPATH, '//div/input[@placeholder="Last Name"]')
    INPUT_FIELD_EMAIL = (By.XPATH, '//*[contains(text(),\'Email\')]/../..//input')
    INPUT_FIELD_PHONE_NUMBER = (By.XPATH, '//*[contains(text(), "Mobile")]/../..//input')
    RADIO_GENDER_MALE = (By.XPATH, '//*[contains(text(), "Male")]')
    RADIO_GENDER_FEMALE = (By.XPATH, '//*[contains(text(), "Female")]')
    RADIO_GENDER_OTHER = (By.XPATH, '//*[contains(text(), "Other")]')
    FLAG_HOBBY_SPORTS = (By.XPATH, '//*[contains(text(), "Sports")]')
    FLAG_HOBBY_READING = (By.XPATH, '//*[contains(text(), "Reading")]')
    FLAG_HOBBY_MUSIC = (By.XPATH, '//*[contains(text(), "Music")]')
    INPUT_FIELD_DOB = (By.XPATH, '//*[contains(text(), \'Date of Birth\')]/../..//input')
    OBJECT_DATEPICKER = (By.XPATH, '//*[@class="react-datepicker"]')
    FIELD_SUBJECTS = (By.XPATH, '//*[contains(text(), "Subjects")]/../../div/div/div')
    DROPDOWN_SUBJECT_LIST = (By.XPATH, '//*[@id="subjectsWrapper"]/*[2]/*/*[3]')
    SUBJECT_ELEMENT_1ST = (By.XPATH, '//*[@id="subjectsContainer"]/*[2]/*[1]/*[1]')
    BUTTON_ATTACH_PICTURE = (By.XPATH, '//*[contains(text(), "Picture")]/../..//input')
    INPUT_FIELD_ADDRESS = (By.XPATH, '//*[contains(text(), "Current")]/../..//textarea')
    DROPDOWN_STATE = (By.XPATH, '//*[contains(text(), "Select State")]/..')
    DROPDOWN_STATE_LIST = (By.XPATH, '//*[@id="stateCity-wrapper"]/*[2]/*/*[3]')
    DROPDOWN_STATE_1ST = (By.XPATH, '//*[@id="stateCity-wrapper"]/*[2]/*/*[3]/*/*[1]')
    DROPDOWN_CITY = (By.XPATH, '//*[contains(text(), "Select City")]/..')
    DROPDOWN_CITY_LIST = (By.XPATH, '//*[@id="stateCity-wrapper"]/*[3]/*/*[3]')
    DROPDOWN_CITY_1ST = (By.XPATH, '//*[@id="stateCity-wrapper"]/*[3]/*/*[3]/*/*[1]')
    OBJECT_SUBMITTED_INFO = (By.XPATH, "//*[contains(text(), 'Thanks for submitting the form')]")
    BUTTON_SUBMIT = (By.XPATH, '//*[contains(text(), "Submit")]')
    BUTTON_CLOSE = (By.XPATH, '//*[contains(text(), "Close")]')


class LocatorsWebtables:

    """Locators for https://demoqa.com/webtables"""

    def set_metadata(self, value):
        self._person_name = value
    _person_name = ""

    @property
    def BUTTON_EDIT(self):
        return By.XPATH, f"//*[@class='rt-table']/*[2]//*[contains(text(), '{self._person_name}')]/..//*[@title='Edit']"

    @property
    def BUTTON_DELETE(self):
        return By.XPATH, f"//*[@class='rt-table']/*[2]//*[contains(text(), '{self._person_name}')]/..//*[" \
                         f"@title='Delete']"

    @property
    def TABLE_FIELD_FIRST_NAME(self):
        return By.XPATH, f"//*[@class=\"rt-table\"]/*[2]//*[contains(text(), '{self._person_name}')]/../*[1]"

    @property
    def TABLE_FIELD_LAST_NAME(self):
        return By.XPATH, f"//*[@class=\"rt-table\"]/*[2]//*[contains(text(), '{self._person_name}')]/../*[2]"

    @property
    def TABLE_FIELD_AGE(self):
        return By.XPATH, f"//*[@class=\"rt-table\"]/*[2]//*[contains(text(), '{self._person_name}')]/../*[3]"

    @property
    def TABLE_FIELD_EMAIL(self):
        return By.XPATH, f"//*[@class=\"rt-table\"]/*[2]//*[contains(text(), '{self._person_name}')]/../*[4]"

    @property
    def TABLE_FIELD_SALARY(self):
        return By.XPATH, f"//*[@class=\"rt-table\"]/*[2]//*[contains(text(), '{self._person_name}')]/../*[5]"

    @property
    def TABLE_FIELD_DEPARTMENT(self):
        return By.XPATH, f"//*[@class=\"rt-table\"]/*[2]//*[contains(text(), '{self._person_name}')]/../*[6]"

    BUTTON_ADD = (By.XPATH, '//*[contains(text(), "Add")]')
    INPUT_FIELD_FIRST_NAME = (By.XPATH, '//*[contains(text(), "First Name")]/../..//input')
    INPUT_FIELD_LAST_NAME = (By.XPATH, '//*[contains(text(), "Last Name")]/../..//input')
    INPUT_FIELD_EMAIL = (By.XPATH, '//*[contains(text(), "Email")]/../..//input')
    INPUT_FIELD_AGE = (By.XPATH, '//*[contains(text(), "Age")]/../..//input')
    INPUT_FIELD_SALARY = (By.XPATH, '//*[contains(text(), "Salary")]/../..//input')
    INPUT_FIELD_DEPARTMENT = (By.XPATH, '//*[contains(text(), "Department")]/../..//input')
    BUTTON_SUBMIT = (By.XPATH, '//*[contains(text(), "Submit")]')



