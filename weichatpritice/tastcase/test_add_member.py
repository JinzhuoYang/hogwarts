import time

from weichatpritice.page.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.main_page = MainPage()

    def test_add_member(self):
        id = str(time.time())
        phone = "17740968102"

        self.main_page.goto_add_member().add_member("xx", id, phone)

