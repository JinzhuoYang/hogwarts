"""
1.把selenium操作放入Basepage中。进行初始化
2.子类会主动调用init
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if not driver:
            url = "https://work.weixin.qq.com/"
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.get(self.url)
            self.driver.implicitly_wait(10)
            # 如果传递了driver，说明不是第一次调用，则不进行初始化
        else:
            self.driver = driver

    def find_by_x(self, x):
        return self.driver.find_element_by_xpath(x)



