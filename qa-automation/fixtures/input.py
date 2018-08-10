from modules.new_userdata import  NewUserData
import time

class InputHelper:

    def __init__(self, app):
        self.app = app


    def add_new_user_input(self, NewUserData):
        wd = self.app.wd
        #Password
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[4]/div/input').click()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[4]/div/input').clear()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[4]/div/input').send_keys(NewUserData.new_password)
        # Tap to side
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[1]').click()
        time.sleep(1)
        #E-mail
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[3]/div/input').click()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[3]/div/input').clear()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[3]/div/input').send_keys(NewUserData.new_email)
        # Tap to side
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[1]').click()
        time.sleep(1)
        #Last name
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[2]/div/input').click()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[2]/div/input').clear()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[2]/div/input').send_keys(NewUserData.last_name)
        # Tap to side
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[1]').click()
        time.sleep(1)
        #First name
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[1]/div/input').click()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[1]/div/input').clear()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[1]/div/input').send_keys(NewUserData.first_name)
        #Tap to side
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[1]').click()
        time.sleep(1)
        # save button
        wd.find_element_by_xpath(
            '//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[9]/div[2]/div/button[2]').click()
        time.sleep(5)