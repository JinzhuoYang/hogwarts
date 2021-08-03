from time import sleep

import selenium
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestLoin:
    def test_remote_chrome(self):
        """
        使用浏览器服用的方式登录
        :return:
        """
        option = Options()
        option.debugger_address = "localhost:9222"
        driver = webdriver.Chrome(options=option)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        sleep(2)
        cookie_var = driver.get_cookies()
        yaml.safe_dump(cookie_var, open("cookie.yaml", mode="w", encoding="utf-8"))
        print(cookie_var)
        # driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()

    def test_cookie_login(self):
        cookie_var = yaml.safe_load(open("cookie.yaml", encoding="utf-8"))
        print(cookie_var)
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookie_var:
            driver.add_cookie(cookie)
        sleep(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")




