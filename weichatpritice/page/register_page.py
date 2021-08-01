from weichatpritice.page.base_page import BasePage


class RegisterPage(BasePage):
    def register(self):
        """
        进行注册
        :return:
        """
        self.driver.find_element_by_xpath('//*[@id="corp_name"]').send_keys("aaaaa")
