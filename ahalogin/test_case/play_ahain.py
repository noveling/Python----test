from selenium import webdriver
from pages.login import Login_page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_ahain(name="三阳路20号",pwd="777777"):
    # opt=webdriver.FirefoxOptions()
    # opt.set_headless()
    driver=webdriver.Firefox()
    test=Login_page(driver,"http://www.codeaha.com/")
    test.gotoFirstPage()
    test.firstLogin()
    test.ahafirstin()

    test.aha_sendInfo(name,pwd)
    test.ahalastin()
    try:
        name=WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app-navbar-collapse"]/ul[2]/li[2]/div/div[1]/a/span[2]')))
        print("登录成功！用户:%s"%name.text)
    except:
        print("没有定位到元素")
    driver.refresh()
    driver.quit()

