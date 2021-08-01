from weichatpritice.page.base_page import BasePage
from weichatpritice.page.login_page import LoginPage
from weichatpritice.page.register_page import RegisterPage


class OfficialPage(BasePage):
    def goto_login(self):
        # "进入登录页面"
        self.driver.find_element_by_xpath('//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        return LoginPage(self.driver)



    def goto_register(self):
        # "进入注册页面"
        self.driver.find_element_by_xpath('//*[@id="tmp"]/div[1]/a').click()
        return RegisterPage(self.driver)