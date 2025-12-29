from .base_page import BasePage
from .locators import BoardsPageLocators


class BoardsPage(BasePage):
    def go_to_board(self):
        go_to_board_btn = self.browser.find_element(*BoardsPageLocators.GO_TO_BOARD_BUTTON)
        go_to_board_btn.click()

    def should_be_board(self):
        assert "board/" in self.browser.current_url, "There is no 'board/' in page url"    