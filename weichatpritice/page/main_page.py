from weichatpritice.page.add_member_page import AddMemberPage
from weichatpritice.page.base_page import BasePage


class MainPage(BasePage):
    url = "https://work.weixin.qq.com/wework_admin/frame"
    def goto_add_member(self):
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        return AddMemberPage(self.driver)

    def goto_import_address(self):
        pass

    def goto_join_member(self):
        pass
