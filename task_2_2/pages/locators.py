from selenium.webdriver.common.by import By


class BasePageLocators:
    CREATE_TASK_BUTTON = (By.CSS_SELECTOR, ".css-897zks")
    BOARDS_BUTTON = (By.CSS_SELECTOR, ":nth-child(2).css-7dkg4p")


class TaskCreationLocators:
    TASK_NAME = (By.CSS_SELECTOR, ".css-1pk1fka")
    TASK_DESCRIPTION = (By.CSS_SELECTOR, ".css-s63k3s")
    BOARD_NAME_LIST = (By.CSS_SELECTOR, "div.css-yd8sa2 > div:nth-child(3).css-17qa0m8")
    BOARD_NAME_LIST_OPTION = (By.CSS_SELECTOR, '[data-value="1"]')
    PRIORITY_LIST = (By.CSS_SELECTOR, "div.css-yd8sa2 > div:nth-child(4).css-17qa0m8")
    PRIORITY_LIST_OPTION = (By.CSS_SELECTOR, '[data-value="Low"]')
    EXECUTOR_LIST = (By.CSS_SELECTOR, "div.css-yd8sa2 > div:nth-child(6).css-17qa0m8")
    EXECUTOR_LIST_OPTION = (By.CSS_SELECTOR, '[data-value="1"]')
    CREATE_BUTTON = (By.CSS_SELECTOR, "div.css-yd8sa2 > div:nth-child(7) .css-iafu2n")

class IssuesPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, ".css-1m7embp")
    BOARD_PANEL = (By.CSS_SELECTOR, ".css-atox0b")

class TaskCardLocators:
    TASK_CARD_BOX_LOCATOR = (By.CSS_SELECTOR, ".css-1epuubg")

class BoardsPageLocators:
    GO_TO_BOARD_BUTTON = (By.CSS_SELECTOR, ".css-1c69r7k")
       