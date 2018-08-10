import time


class SelectorHelper:

    def __init__(self, app):
        self.app = app


    def add_new_user_select(self):
        wd = self.app.wd
        # Path to adding user
        wd.find_element_by_xpath('//*[@id="wrapper"]/div[1]/nav/ul/li[6]/a').click()
        wd.find_element_by_xpath('//*[@id="wrapper"]/div[1]/nav/ul/li[6]/ul/li[2]/a').click()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div[1]/div/div/button').click()
        # Country selector
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[6]/div/select').click()
        time.sleep(1)
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[6]/div/select/option[3]').click()
        time.sleep(1)
        # Tap to side
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[1]').click()
        time.sleep(1)
        # Role selector
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[5]/div/select').click()
        time.sleep(1)
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[5]/div/select/option[15]').click()
        time.sleep(1)
        # Tap to side
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[1]').click()
        time.sleep(1)