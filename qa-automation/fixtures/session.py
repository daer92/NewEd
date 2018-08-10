import time
from modules.logindata import UserData

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_process(self, User_Data):
        wd = self.app.wd
        wd.find_element_by_name("mxEmail").click()
        wd.find_element_by_name("mxEmail").clear()
        wd.find_element_by_name("mxEmail").send_keys(User_Data.username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(User_Data.password_key)
        wd.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(5)



    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="wrapper"]/div[1]/nav/div[3]/div/div[1]').click()
        time.sleep(5)


