from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
from .locators import TaskCreationLocators
import time


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how_to_find, locator_to_find):
        try:
            self.browser.find_element(how_to_find, locator_to_find)
        except NoSuchElementException:
            return False
        else:
            return True

    def go_to_task_creation(self):
        link = self.browser.find_element(*BasePageLocators.CREATE_TASK_BUTTON)
        link.click()

    def go_to_boards_page(self):
        link = self.browser.find_element(*BasePageLocators.BOARDS_BUTTON)
        link.click()

    def create_task(self, name):
        task_name = self.browser.find_element(*TaskCreationLocators.TASK_NAME)
        task_name.send_keys(name)
        tsak_description = self.browser.find_element(*TaskCreationLocators.TASK_DESCRIPTION)
        tsak_description.send_keys('description')
        board_name = self.browser.find_element(*TaskCreationLocators.BOARD_NAME_LIST)
        board_name.click()
        board_name_option = self.browser.find_element(*TaskCreationLocators.BOARD_NAME_LIST_OPTION)
        board_name_option.click()
        priority = self.browser.find_element(*TaskCreationLocators.PRIORITY_LIST)
        priority.click()
        priority_option = self.browser.find_element(*TaskCreationLocators.PRIORITY_LIST_OPTION)
        priority_option.click()
        executor = self.browser.find_element(*TaskCreationLocators.EXECUTOR_LIST)
        executor.click()
        executor_option = self.browser.find_element(*TaskCreationLocators.EXECUTOR_LIST_OPTION)
        executor_option.click()
        create_button = self.browser.find_element(*TaskCreationLocators.CREATE_BUTTON)
        create_button.click()
        time.sleep(2)
