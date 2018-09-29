from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import requests


def getahastorage(name, pwd):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("http://www.codeaha.com/")

    # 点登录
    login1 = driver.find_element_by_xpath(
        "//*[@id='app-navbar-collapse']/ul[2]/li[1]")
    login1.click()
    aha = WebDriverWait(
        driver, 10, 0.2).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='third-party text-center']/span[3]")))
    aha.click()
    ahaname = driver.find_element_by_xpath(
        '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[1]/section[5]/div[1]/div[1]/div/input')
    ahapwd = driver.find_element_by_xpath(
        '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[1]/section[5]/div[2]/div[1]/div/input')
    ahaname.send_keys(name)
    ahapwd.send_keys(pwd)
    loginbutton = driver.find_element_by_xpath(
        '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[1]/section[5]/div[3]/div/button')
    loginbutton.click()
    try:
        name = WebDriverWait(
            driver,
            15).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div[2]/div/div[2]/div[1]/nav/div/div[2]/ul[2]/li[2]/div/div[1]/a/span[2]')))
        print(name.text)
    except BaseException:
        print("没有定位到元素！")
        driver.quit()
        exit(1)

    js = '''
    var info = window.localStorage["aha_token"];
    document.title = info;
    '''

    driver.execute_script(js)
    res = driver.title
    driver.quit()
    print(res)
    rel = json.loads(res)
    val = rel["content"]
    return val


def getstorage(name, pwd):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("http://www.codeaha.com/")

    # 点登录
    login1 = driver.find_element_by_xpath(
        "//*[@id='app-navbar-collapse']/ul[2]/li[1]")
    login1.click()
    qq = WebDriverWait(
        driver, 10, 0.2).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='third-party text-center']/span[1]")))
    qq.click()
    time.sleep(3)
    print(driver.title)
    driver.switch_to.window(driver.window_handles[1])
    driver.switch_to.frame("ptlogin_iframe")
    print(driver.find_element_by_id('switcher_plogin').text)
    driver.find_element_by_id('switcher_plogin').click()

    # 输入账号
    qqnum = driver.find_element_by_id("u")
    qqnum.send_keys(name)
    qqpwd = driver.find_element_by_id("p")
    qqpwd.send_keys(pwd)
    driver.find_element_by_id("login_button").click()
    driver.switch_to.window(driver.window_handles[0])
    driver.switch_to.default_content()
    try:
        name = WebDriverWait(
            driver,
            15).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div[2]/div/div[2]/div[1]/nav/div/div[2]/ul[2]/li[2]/div/div[1]/a/span[2]')))
        print(name.text)
    except BaseException:
        print("没有定位到元素！")
        driver.quit()
        exit(1)

    js = '''
    var info = window.localStorage["aha_token"];
    document.title = info;
    '''

    driver.execute_script(js)
    res = driver.title
    driver.quit()
    print(res)
    rel = json.loads(res)
    val = rel["content"]
    return val
    # regex = re.compile(r'"content":"(.*?)"',re.S)
    # val = regex.findall(res)
    # print(val)
    # return val


def quickpass(val, num=1):
    headers = {
        "Authorization": val
    }
    data = {
        "level": num,
        "score": "2"
    }
    response = requests.post(
        url="http://www.codeaha.com/api/game/update_game_info",
        data=data,
        headers=headers)
    return response


if __name__ == "__main__":
    #通过aha账号
    # auth = getahastorage(name="ahateacher1", pwd="***********")
    #通过qq账号
    auth = getstorage("??????","??????")
    for i in range(1, 62):
        result = quickpass(auth, i)
        try:
            rel = json.loads(result.text)
            print("stage:" + str(i), rel)
        except BaseException:
            print("stage:" + str(i), result.text)
