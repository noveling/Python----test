from .common import Page
from selenium.webdriver.common.by import By


class Login_page(Page):
    username = (By.NAME, "admin_username")
    userpwd = (By.NAME, "admin_password")
    submit = (By.NAME, "submit")
    confirm_name = (By.XPATH, "//div[@id='frameuinfo']/p/em")

    def input_info(self, name, pwd):
        self.input_text(self.username, name)
        self.input_text(self.userpwd, pwd)

    def clicksubmit(self):
        self.click(self.submit)

    def goto_firstpage(self):
        self.driver.get(self.base_url)
