from .base_page import BasePage
from .locators import IssuesPageLocators
from .locators import TaskCardLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IssuesPage(BasePage):
    def should_be_able_to_find_task(self, browser, name_to_find='Оптимизация бандла Webpack'):
        search_field = self.browser.find_element(*IssuesPageLocators.SEARCH_INPUT)
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((search_field))
            )
        search_field.send_keys(name_to_find)
        assert self.is_element_present(By.XPATH, f"//h6[text()='{name_to_find}']"), "The searched task wasn't found"

    def create_task_from_issues_page(self, name):
        self.go_to_task_creation()
        self.create_task(name)

    def should_be_able_to_open_task_card(self):
        board_panel = self.browser.find_element(*IssuesPageLocators.BOARD_PANEL)
        board_panel.click()
        assert self.is_element_present(*TaskCardLocators.TASK_CARD_BOX_LOCATOR), "The task card wasn't found"


        
