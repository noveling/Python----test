from common.base import Page
from selenium.webdriver.common.by import By


class Login_page(Page):
    # 首页登录
    first_login = (By.XPATH, "//*[@id='app-navbar-collapse']/ul[2]/li[1]")
    # 界面跳转第三方登录
    second_login = (By.XPATH, "//div[@class='third-party text-center']/span[1]")
    aha_second_login = (By.XPATH, "//div[@class='third-party text-center']/span[3]")

    # 继续点链接
    third_login = (By.ID, 'switcher_plogin')
    # 继续...
    forth_login = (By.ID, 'login_button')
    aha_lastin = (By.XPATH,"/html/body/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[1]/section[5]/div[3]/div/button")
    # input框
    name_in = (By.ID, "u")
    pwd_in = (By.ID, "p")

    aha_name = (By.XPATH,"/html/body/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[1]/section[5]/div[1]/div[1]/div/input")
    aha_pwd = (By.XPATH,"/html/body/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[1]/section[5]/div[2]/div[1]/div/input")

    def __init__(self,driver,base_url="http://www.codeaha.com/"):
        Page.__init__(self,driver,base_url)

    def gotoFirstPage(self):
        print("打开首页%s"%self.base_url)
        self.driver.get(self.base_url)

    def ahafirstin(self):
        self.click(self.aha_second_login)

    def firstLogin(self):
        self.click(self.first_login)

    def secondLogin(self):
        self.click(self.second_login)

    def thirdLogin(self):
        self.click(self.third_login)

    def forthLogin(self):
        self.click(self.forth_login)

    def sendInfo(self,name,pwd):
        self.input_text(self.name_in,name)
        self.input_text(self.pwd_in,pwd)

    def aha_sendInfo(self,name,pwd):
        self.input_text(self.aha_name, name)
        self.input_text(self.aha_pwd, pwd)

    def ahalastin(self):
        self.click(self.aha_lastin)

