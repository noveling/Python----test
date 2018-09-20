import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import send_mail

test_dir = "./test_case/"
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py",top_level_dir=None)

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M")
    filename = "./report/" + '/' + now + "result.html"
    fp = open(filename,'wb')

    runner = HTMLTestRunner(stream=fp,title="测试报告",description="用例情况:",verbosity=2)
    runner.run(discover)
    fp.close()
    send_mail.sendmail("1668858001@qq.com")