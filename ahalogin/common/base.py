
class Page(object):
    ''' 所有page的基类 '''
    def __init__(self,driver,base_url="http://www.codeaha.com/"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 10
        self.driver.implicitly_wait(self.timeout)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def input_text(self,loc,text):
        self.find_element(*loc).send_keys(text)

    def click(self,loc):
        self.find_element(*loc).click()

    def get_title(self):
        return self.driver.title