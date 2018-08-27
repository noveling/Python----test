# 生成添柴账号

import requests
import re
import getemail

# from admin_login import play_login


url = "http://bbs.codeaha.com/admin.php?action=members&operation=add"

cookie = "AZeK_7ffe_saltkey=j5uDkBC3;" \
         " AZeK_7ffe_lastvisit=1530581359; " \
         "AZeK_7ffe_visitedfid=41D106;" \
         " AZeK_7ffe_nofavfid=1; " \
         "AZeK_7ffe_smile=1D1; " \
         "AZeK_7ffe_lastcheckfeed=61630%7C1531293799;" \
         " Hm_lvt_703d2210aab30d95de944a3b34b48451=1531358328,1531375377,1531382687,1531444748;" \
         " AZeK_7ffe_ulastactivity=1755gCDZ" \
         "WQ%2B8V6lwDkCOU0X7pwrWqRvBI87RQQ" \
         "TI0oLRAGrthqJi; " \
         "AZeK_7ffe_checkupgrade=1;" \
         " AZeK_7ffe_auth=8243bGntQ7ExVbG7hynWvwzPPMprVRirbt7viMWF71OX8NSNgd1IZhXYJdxBOWIPC9oM2gIZXZbU8b3uLWUXd4g;" \
         " AZeK_7ffe_lip=59.175.19.24%2C1531451121; AZeK_7ffe_lastact=1531451190%09admin.php%09; AZeK_7ffe_sid=rLxP9O;"


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.2.17331",
    "Cookie": cookie,

}


def register(username, userpwd, useremail):
    data = {
        "formhash": "490065ec",
        "scrolltop": "",
        "anchor": u"",
        "newusername": username,
        "newpassword": userpwd,
        "newemail": useremail,
        "newgroupid": 10,
        "emailnotify": 0,
        "addsubmit": "(unable to decode value)"

    }
    print(useremail)
    reg = re.compile(r'''<h4 class="infotitle2">用户 (.*?) 添加成功''', re.S)
    response = requests.post(url=url, data=data, headers=header)
    res = reg.findall(response.text)
    if res:
        for i in res:
            print(''.join(["用户： ", i]))
    else:
        print("注册失败！")
        print(response.text)


if __name__ == "__main__":
    # play_login.play_login()

    # with open("C:\\Users\\Administrator\\Desktop\\6.txt", "r") as fp:
    #     i = 26
    #     for f in fp:
    #         email = getemail.getemail()
    #         name = ("Gz"+str(i)).rstrip("\n").encode('gbk')  # 输入的编码方式gbk
    #         print("密码:"+f.strip("\n"))
    #         print(name.decode('gbk'))
    #         register(username=name, userpwd=f, useremail=email)
    #         i += 1
    with open("C:\\Users\\Administrator\\Desktop\\7.txt", "r") as fp:
        pwd = "pythonlearning"
        for i in fp:
            name = "三阳路_"+i.strip('\n')
            email = getemail.getemail()
            register(username=name.encode('gbk'), userpwd=pwd, useremail=email)
            print("账号:" + name + " 密码:" + pwd + " 邮箱:" + email)
