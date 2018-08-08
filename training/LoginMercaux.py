# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import unittest, time



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
        self.login_process(wd)
        self.assertTrue(success)


    def login_process(self, wd):
        wd.find_element_by_name("mxEmail").click()
        wd.find_element_by_name("mxEmail").clear()
        time.sleep(5)
        wd.find_element_by_name("mxEmail").send_keys("ilya-benetton@mercaux.com")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        time.sleep(5)
        wd.find_element_by_name("password").send_keys("123321")
        wd.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()


    def open_home_page(self, wd):
        wd.get("https://stg.mercaux.com/#/login")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main


"""Login first test"""

