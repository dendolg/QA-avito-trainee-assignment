import pytest
from .pages.issues_page import IssuesPage
from .pages.boards_page import BoardsPage
import time


class TestUserCanCreateTask():
    def test_user_can_create_task(self, browser):
        name = str(time.time()) + " unique name"
        link = "https://avito-tech-internship-psi.vercel.app/"
        page = IssuesPage(browser, link)
        page.open()
        page.create_task_from_issues_page(name)
        page.should_be_able_to_find_task(name)


class TestUserCanOpenTaskCard():
    def test_user_can_open_task_card_from_issues_page(self, browser):
        link = "https://avito-tech-internship-psi.vercel.app/"
        page = IssuesPage(browser, link)
        page.open()
        page.should_be_able_to_open_task_card()


class TestUserCanFindTask():
    def test_user_can_find_task(self, browser):
        link = "https://avito-tech-internship-psi.vercel.app/"
        page = IssuesPage(browser, link)
        page.open()
        page.should_be_able_to_find_task(browser)


class TestUserCanOpenBoard():
    def test_user_can_open_board_from_issues_page(self, browser):
        link = "https://avito-tech-internship-psi.vercel.app/"
        page = IssuesPage(browser, link)
        page.open()
        page.go_to_boards_page()
        boards_page = BoardsPage(browser, browser.current_url)
        boards_page.go_to_board()
        boards_page.should_be_board()

    
