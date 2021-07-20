'''
通过百度搜索芒果TV，执行一系列操作，打开说唱听我的并开始播放
'''

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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
        print(self.driver.window_handles)
        self.driver.find_element(By.XPATH,'//*[@id=1]//a[1]').click()
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element(By.XPATH,'//*[@id="privacy-policy"]//button[2]').click()
        self.driver.find_element_by_xpath('//*[@id="m-topheader"]/div/div[1]/div/input').send_keys('说唱听我的')
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[3]/div[1]/div[1]/div[1]/div/div[2]/p[1]/a/span').click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[2]/div/div[1]/div[2]/div[4]/a[1]').click()
