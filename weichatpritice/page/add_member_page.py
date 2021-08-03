from weichatpritice.page.base_page import BasePage


class AddMemberPage(BasePage):
    def add_member(self, username, acctid, phone):
        """
        添加成员
        :param username: 成员名字
        :param acctid: 唯一ID
        :param phone: 手机号
        :return:
        """
        self.find_by_x('//*[@id="username"]').send_keys(username)
        self.find_by_x('//*[@id="memberAdd_acctid"]').send_keys(acctid)
        self.find_by_x('//*[@id="memberAdd_phone"]').send_keys(phone)
        self.find_by_x('//*[contains(@class,"js_btn_save")]').click()
