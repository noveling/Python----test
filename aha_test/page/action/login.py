from ..common import base
from selenium.webdriver.common.by import By

class tkPage(base):
    login = (By.XPATH,"//*[@id='nv_plugin']/div[3]/div/div[3]/div/a")



    #点图标
    def login(self):
        self.find_element(*self.login).click()

    #定义统一登录入口
    def user_login(self):
        self.login()