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


    def add_new_user_select(self):
        wd = self.wd
        #Path to adding user
        wd.find_element_by_xpath('//*[@id="wrapper"]/div[1]/nav/ul/li[6]/a').click()
        wd.find_element_by_xpath('//*[@id="wrapper"]/div[1]/nav/ul/li[6]/ul/li[2]/a').click()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div[1]/div/div/button').click()
        #Country selector
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[6]/div/select').click()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[6]/div/select/option[3]').click()
        # Tap to side
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[1]').click()
        # Role selector
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[5]/div/select').click()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[5]/div/select/option[15]').click()
        # Tap to side
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[1]').click()


    def add_new_user_input(self, NewUserData):
        wd = self.wd
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
        #Last name
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[2]/div/input').click()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[2]/div/input').clear()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[2]/div/input').send_keys(NewUserData.last_name)
        # Tap to side
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[1]').click()
        #First name
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[1]/div/input').click()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[1]/div/input').clear()
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[1]/div/input').send_keys(NewUserData.first_name)
        #Tap to side
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[1]').click()
        #save button
        wd.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/div/div[2]/form/div[9]/div[2]/div/button[2]').click()
        time.sleep(5)







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



