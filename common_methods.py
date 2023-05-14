from selenium.webdriver import Keys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class Methods:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 4)

    """Find element by locator"""
    def find(self, element):
        return self.wait.until(EC.visibility_of_element_located(element))

    """Checks if element exists"""
    def locator_is_present(self, element) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(element))
            return True
        except TimeoutException:
            return False

    """Click the element."""
    def click(self, element):
        self.find(element).click()

    """Click the element, then enter a text."""
    def click_and_input(self, element, text: str):
        self.click(element)
        self.driver.switch_to.active_element.send_keys(text)
        pass

    """Input text into a current active element."""
    def input_text(self, element, text: str):
        self.find(element).send_keys(text)
        pass

    """Clear the text. it uses keyboard emulation for authentic user-like input."""
    def clear_here(self):
        self.driver.switch_to.active_element.send_keys(Keys.CONTROL, "a")
        self.driver.switch_to.active_element.send_keys(Keys.BACKSPACE)

    """Emulate pressing of ENTER key."""
    def press_enter_here(self):
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)

    """Clicking the element and replacing it with a text."""
    def click_and_replace(self, element, text: str):
        self.click(element)
        self.replace_here(text)

    """Replacing a text input in a current active element."""
    def replace_here(self, text: str):
        self.driver.switch_to.active_element.send_keys(Keys.CONTROL, "a")
        self.driver.switch_to.active_element.send_keys(text)

    """Input text into a current focused field."""
    def input_text_here(self, text: str):
        self.driver.switch_to.active_element.send_keys(text)

    """Upload a file. It searches the file in a project folder."""
    def unload_file(self, element, file_path: str):
        self.find(element).send_keys(os.getcwd() + "/" + file_path)

    """Emitting a click on element. Instead of just clicking element, it moves the pointer on top of that element, 
    then clicking. The x and y variables allows to offset the click in case if the centre of element is partially 
    covered."""
    def click_with_offset(self, element, x=0, y=0):
        ActionChains(self.driver).move_to_element_with_offset(self.find(element), x, y).click().perform()

    """Get element text. Returns string"""
    def get_element_text(self, element) -> str:
        return self.find(element).text

    """Compare element text with a sample text. Returns bool."""
    def compare_element_text_with(self, element, text: str) -> bool:
        return self.get_element_text(element) == text
        pass


"""A helper class, allows to use multiple assertions in a same test, without stopping the script after a first error. 
It also provides the list of errors occured."""
class MultiAssertHandler:
    def __init__(self):
        self.errors = ""
        self.failed = False
        self.counter = 0

    def assert_single(self, check_value, message=""):
        self.counter += 1
        if not check_value:
            """If user set the error message - adds message to a list of messages. Otherwise index of error."""
            self.errors += "\n"
            self.errors += f"Unnamed error, assertion #{str(self.counter)}" if message == "" else message
            self.failed = True

    def is_successful(self) -> bool:
        return not self.failed

    def retrieve_errors(self) -> [bool]:
        return self.errors
