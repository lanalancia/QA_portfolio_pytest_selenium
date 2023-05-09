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

    # Найти элемент по локатору
    def find(self, element):
        return self.wait.until(EC.visibility_of_element_located(element))

    # Проверяет, можно ли найти элемент. Возвращает элемент или False
    def locator_is_present(self, element):
        try:
            self.wait.until(EC.visibility_of_element_located(element))
            return True
        except TimeoutException:
            return False

    # Кликнуть по элементу
    def click(self, element):
        self.find(element).click()

    # Кликнуть по элементу и ввести текст в этот элемент (например, если нужно ввести текст в поле)
    def click_and_input(self, element, text: str):
        self.click(element)
        self.driver.switch_to.active_element.send_keys(text)
        pass

    # ввести текст в элемент независимо от того, в фокусе он или нет
    def input_text(self, element, text: str):
        self.find(element).send_keys(text)
        pass

    # Очистить текст с помощью ввода на клавиатуре.
    def clear_here(self):
        self.driver.switch_to.active_element.send_keys(Keys.CONTROL, "a")
        self.driver.switch_to.active_element.send_keys(Keys.BACKSPACE)

    # Нажать Enter на клавиатуре. Используется как один из способов выбрать первый элемент списка
    def press_enter_here(self):
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)

    # Нажать на поле и заменить текст в этом поле другим текстом
    def click_and_replace(self, element, text: str):
        self.click(element)
        self.replace_here(text)

    # Заменить текст в элементе, на котором сейчас фокус, другим текстом
    def replace_here(self, text: str):
        self.driver.switch_to.active_element.send_keys(Keys.CONTROL, "a")
        self.driver.switch_to.active_element.send_keys(text)

    # Ввод текста в элемент, который находится в фокусе
    def input_text_here(self, text: str):
        self.driver.switch_to.active_element.send_keys(text)

    # Загрузка файла с помощью send_keys. Файл загружается из папки с репозиторием
    def unload_file(self, element, file_path: str):
        self.find(element).send_keys(os.getcwd() + "/" + file_path)

    # Кликнуть по кнопке со смещением курсора. Используется если центр кнопки перекрыт другими элементами
    def click_with_offset(self, element, x=0, y=0):
        ActionChains(self.driver).move_to_element_with_offset(self.find(element),
                                                              x, y).click().perform()

    # Получить текст элемента, нужно для assert
    def get_element_text(self, element):
        return self.find(element).text

    # Сравнить текст элемента с текстом в параметрах
    def compare_element_text_with(self, element, text: str):
        return self.get_element_text(element) == text
        pass


# Этот класс нужен чтобы сделатть множество assert в одном автотесте, не прекращая его исполнение после первой ошибки.
# После выполнения теста будут отображены ошибки, которые были обнаружены.
# Если в assert_single не будет указан параметр message, но ошибка произошла - будет выведен порядковый номер ассёрта.
class MultiAssertHandler:
    def __init__(self):
        self.errors = ""
        self.failed = False
        self.counter = 0

    def assert_single(self, check_value, message=""):
        self.counter += 1
        if not check_value:
            # Если сообщение об ошибке передано через параметр - выводится сообщение.
            # Если сообщение не было передано - заменяется на дефолтное + порядковый номер вызова assert_single.
            # Это QOL feature.
            self.errors += "\n"
            self.errors += f"Unnamed error, assertion #{str(self.counter)}" if message == "" else message
            self.failed = True

    def is_successful(self) -> bool:
        return not self.failed

    def retrieve_errors(self) -> [bool]:
        return self.errors
