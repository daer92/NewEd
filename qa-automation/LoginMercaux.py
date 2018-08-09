# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import unittest, time
from User_Data import UserData


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False
    return False

class FirstLoginTest(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)


    def test_login(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login_process(wd, UserData(username="ilya-benetton@mercaux.com", password_key="123321"))
        self.assertTrue(success)
        self.logout(wd)


    def test_incorrect_login(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login_process(wd, UserData(username="dddd@incorrect.com", password_key="2222222"))
        self.assertTrue(success)


    def logout(self, wd):
        wd.find_element_by_xpath('//*[@id="wrapper"]/div[1]/nav/div[3]/div/div[1]').click()
        time.sleep(5)

    def login_process(self, wd, User_Data):
        wd.find_element_by_name("mxEmail").click()
        wd.find_element_by_name("mxEmail").clear()
        wd.find_element_by_name("mxEmail").send_keys(User_Data.username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(User_Data.password_key)
        wd.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(5)

    def open_home_page(self, wd):
        wd.get("https://stg.mercaux.com/#/login")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main


"""Login first test"""

