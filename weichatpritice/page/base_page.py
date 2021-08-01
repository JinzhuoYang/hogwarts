"""
1.把selenium操作放入Basepage中。进行初始化
2.子类会主动调用init
"""
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if not driver:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/")
            self.driver.implicitly_wait(10)
            # 如果传递了driver，说明不是第一次调用，则不进行初始化
        else:
            self.driver = driver


