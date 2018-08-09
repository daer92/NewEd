from selenium.webdriver.chrome.webdriver import WebDriver
import time, unittest


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def logout(self):
        wd = self.wd
        wd.find_element_by_xpath('//*[@id="wrapper"]/div[1]/nav/div[3]/div/div[1]').click()
        time.sleep(5)

    def login_process(self, User_Data):
        wd = self.wd
        wd.find_element_by_name("mxEmail").click()
        wd.find_element_by_name("mxEmail").clear()
        wd.find_element_by_name("mxEmail").send_keys(User_Data.username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(User_Data.password_key)
        wd.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(5)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://stg.mercaux.com/#/login")

    def destroy(self):
        self.wd.quit()

