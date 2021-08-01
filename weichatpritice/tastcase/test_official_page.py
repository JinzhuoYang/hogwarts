from weichatpritice.page.official_page import OfficialPage


class TestOfficialPage:
    def setup(self):
        self.official = OfficialPage()

    def test_goto_login(self):
        self.official.goto_login().scan()

    def test_goto_register(self):
        self.official.goto_register().register()

    def test_goto_login_goto_register(self):
        self.official.goto_login().goto_register().register()