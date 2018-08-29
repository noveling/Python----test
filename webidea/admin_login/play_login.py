from .pages import Login_page
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def play_login():
    driver = webdriver.Firefox()
    test = Login_page(driver,"http://bbs.codeaha.com/admin.php")
    test.goto_firstpage()
    test.input_info("XXX", "XXXXXXX")
    test.clicksubmit()
    try:
        print("用户名: "+WebDriverWait(driver,10,0.2).until(EC.presence_of_element_located(test.confirm_name)).text)
    except:
        print("没有定位到元素")
    # driver.quit()
