# 产生一个随机的email地址

import requests
import random
import time
import re


def randomword():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.2.17331"
    }
    timestamp = int(time.time()*1000)
    url = '''https://suijimimashengcheng.51240.com/web_system/51240_com_www/system/file/suijimimashengcheng/get/?dx=true&xx=true&sz=true&fh=false&fh_value=!%40%23%24%2525%255E%26*&cd=''' + \
        str(random.randint(3, 8)) + '''&ajaxtimestamp='''+str(timestamp)
    response = requests.get(url=url, headers=header)
    reg = re.compile(r'''value="(.*?)"''', re.S)
    res = reg.findall(response.text)
    return res[0]


def getemail():
    return randomword() + "@"+randomword()+".com"


if __name__ == "__main__":
    print(getemail())
