from selenium import webdriver
class Base:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        pass
        # self.driver.quit()
