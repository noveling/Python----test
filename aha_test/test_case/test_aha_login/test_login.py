from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time




class loginin_bank(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        print("啊哈星球登录测试")
    '''测试添柴题库'''
    def setUp(self):
        self.base_url = "http://www.codeaha.com/"



    def test_loginaha(self):
        '''登录aha星球'''
        # 点登录
        self.driver.get(self.base_url)
        login1 = self.driver.find_element_by_xpath("//*[@id='app-navbar-collapse']/ul[2]/li[1]")
        login1.click()
        qq = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[2]/div/div/div[1]/div/div/div[1]/section[1]/div[3]/div/span[1]"))
                                             )
        qq.click()
        # time.sleep(3)
        # print(driver.title)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.switch_to.frame("ptlogin_iframe")
        # print(self.driver.find_element_by_id('switcher_plogin').text)
        time.sleep(2)
        self.driver.find_element_by_id('switcher_plogin').click()

        # 输入账号
        qqnum = self.driver.find_element_by_id("u")
        qqnum.send_keys("2823502386")
        qqpwd = self.driver.find_element_by_id("p")
        qqpwd.send_keys("wdid17xc")
        self.driver.find_element_by_id("login_button").click()
        self.driver.switch_to.window(self.driver.window_handles[0])
        #self.driver.switch_to.default_content() #不行
        time.sleep(4)
        self.driver.refresh()
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app-navbar-collapse"]/ul[2]/li[2]/div/div[1]/a/span[2]')))
        print(self.driver.find_element_by_xpath('//*[@id="app-navbar-collapse"]/ul[2]/li[2]/div/div[1]/a/span[2]').text)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="app-navbar-collapse"]/ul[2]/li[2]/div/div[1]/a/span[2]').text,"psodsa xuche","没有登录上")

    def test_aha(self):
        '''登录aha星球'''
        # 点登录
        self.driver.get(self.base_url)
        time.sleep(2)


    def tearDown(self):
        print("完成该用例")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("结束该场景")
