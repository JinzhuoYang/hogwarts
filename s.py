'''
通过百度搜索芒果TV，执行一系列操作，打开说唱听我的并开始播放
'''
import  selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By


class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass
        # self.driver.quit()

    def test_hogwards(self):
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("芒果TV")
        self.driver.find_element(By.XPATH,'//*[@id="su"]').click()
        self.driver.find_element(By.XPATH,'//*[@id=1]//a[1]').click()
        sleep(10)
        windows = chrome.window_handles
        self.driver.switch_to.window(windows[1])


        self.driver.find_element(By.XPATH,'//*[@id="privacy-policy"]//button[2]').click()