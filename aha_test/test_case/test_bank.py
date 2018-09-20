from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest





class Question_bank(unittest.TestCase):

    '''测试添柴题库'''

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://bbs.codeaha.com/tiku/"


    def test_bank1(self):
        '''添柴题库测试内容：输入搜索id 12003'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("search_text").send_keys("12003")
        driver.find_element_by_id("search_submit_btn").click()
        s_info = WebDriverWait(driver,6,0.2).until\
            (EC.presence_of_element_located((By.LINK_TEXT,"1.3-1混合牛奶")))
        s_info.click()
        self.assertEqual(driver.current_url,"http://bbs.codeaha.com/problem-12003.html","Not Found Page")

    # def test_bank_random(self):
    #     '''添柴题库测试内容：输入搜索id 12003'''
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     driver.find_element_by_id("search_text").send_keys()
    #     driver.find_element_by_id("search_submit_btn").click()
    #     # s_info = WebDriverWait(driver,6,0.2).until\
    #     #     (EC.presence_of_element_located((By.LINK_TEXT,"1.3-1混合牛奶")))
    #     # s_info.click()
    #     # self.assertEqual(driver.current_url,"http://bbs.codeaha.com/problem-12003.html","Not Found Page")
    def test_bank2(self):
        '''添柴题库测试内容：输入搜索标题 解救小哈'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("search_text").send_keys("解救小哈")
        driver.find_element_by_id("search_submit_btn").click()
        s_info = WebDriverWait(driver,6,0.2).until\
            (EC.presence_of_element_located((By.LINK_TEXT,"解救小哈")))
        s_info.click()
        self.assertEqual(driver.current_url,"http://bbs.codeaha.com/problem-12032.html","Not Found Page")

    def test_bank3(self):
        '''添柴题库测试内容：输入搜索tag 字符串'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("search_text").send_keys("字符串")
        driver.find_element_by_id("search_submit_btn").click()
        s_info = WebDriverWait(driver, 6, 0.2).until \
            (EC.presence_of_element_located((By.LINK_TEXT, "手机")))
        s_info.click()
        self.assertEqual(driver.current_url, "http://bbs.codeaha.com/problem-12078.html", "Not Found Page")

    def tearDown(self):
        self.driver.quit()