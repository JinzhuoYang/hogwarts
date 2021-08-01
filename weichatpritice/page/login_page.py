from weichatpritice.page.base_page import BasePage
from weichatpritice.page.register_page import RegisterPage


class LoginPage(BasePage):
    def scan(self):
        """
        扫码
        :return
        """
        pass

    def goto_register(self):
        """
        进入注册页面
        :return:
        """
        self.driver.find_element_by_xpath('//*[@id="wework_admin.loginpage_wx_$"]/main/div[2]/a').click()
        return RegisterPage(self.driver)