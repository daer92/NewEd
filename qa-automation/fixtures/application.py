from selenium.webdriver.chrome.webdriver import WebDriver
import time, unittest
from fixtures.session import SessionHelper
from fixtures.input import InputHelper
from fixtures.selector import SelectorHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.input = InputHelper(self)
        self.selector = SelectorHelper(self)



    def open_home_page(self):
        wd = self.wd
        wd.get("https://stg.mercaux.com/#/login")


    def delete_user(self):
        wd = self.wd
        wd.find_element_by_xpath('//*[@id="wrapper"]/div[1]/nav/ul/li[6]/a').click()
        wd.find_element_by_xpath('//*[@id="wrapper"]/div[1]/nav/ul/li[6]/ul/li[2]/a').click()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div[2]/div/table/tbody[2]/tr[1]/td/div').click()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div[2]/div/table/tbody[6]/tr[1]/td').click()
        wd.find_element_by_css_selector('#page-wrapper > div > div > div > div.mx-page-content > div > table > tbody:nth-child(7) > tr:nth-child(3) > td:nth-child(1)').click()
        time.sleep(10)




    def destroy(self):
        self.wd.quit()



