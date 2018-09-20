from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest





class Question_bank(unittest.TestCase):
    def __init__(self):
        items = [1,2,3]
        for i in items:
            setattr(Question_bank,"test_fun_%s"%i)
            Question_bank.getTestFunc(i)

    '''测试添柴题库'''

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://bbs.codeaha.com/tiku/"

    @staticmethod
    def getTestFunc(str):
        def test_bank1(self):
            '''添柴题库测试内容：输入搜索tag 字符串'''
            driver = self.driver
            driver.get(self.base_url)
            driver.find_element_by_id("search_text").send_keys(str)
            driver.find_element_by_id("search_submit_btn").click()
        return test_bank1



    def tearDown(self):
        self.driver.quit()