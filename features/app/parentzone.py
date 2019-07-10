import os
import sys
from time import sleep
from selenium.webdriver.common.by import By

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../games/templates/'))
from base_class import BaseClass

class Parentzone(BaseClass):
    
    def mychild(self):
        self.tap('MyChildButton')
        try:
            self.driver.find_element(By.XPATH, "//android.view.View[@content-desc='My Child']")
        except:
            self.driver.find_element(By.XPATH, "//android.view.View[@text='My Child']")
        
    def myaccount(self):
        self.tap('MyAccountButton')
        
    def paymentplan(self):
        self.tap('PaymentPlansButton')
    
    def verify_others_section(self,section_name,text):
        print self.driver.context
        self.altdriver.find_element(section_name).tap()
        sleep(3)
        print self.driver.context
#         header = self.driver.find_element_by_xpath("//android.view.View[@instance='78']")
        header = self.driver.find_element_by_xpath("//*[@text='"+text+"']")
        assert header.text in text
        print header.text
        
        
    def verify_rate_us(self,section_name):
        print self.driver.current_activity
        sleep(3)
        self.altdriver.find_element(section_name).tap()
        sleep(6)
        assert  self.driver.current_activity in 'com.google.android.finsky.activities.MainActivity'
        
        
    def click_on_logout(self):
        self.altdriver.find_element('logout').tap()
        
        
    def change_parent_info(self,parent_name):
        self.altdriver.find_element('MyRelationDropDown').tap()
        droplist=self.altdriver.find_elements('Item Label')
        print len(droplist)
        for i in range(len(droplist)):
            if droplist[i].get_text() in parent_name:
                droplist[i].tap()

    def account_details(self,option,email):
        self.altdriver.find_element(option).tap()
        sleep(3)
        self.altdriver.find_element('EmailAdvanceInputField (1)/Text').tap()
        sleep(10)
        self.base_class = BaseClass(self.altdriver, self.driver)
        self.base_class.clear_text('EmailAdvanceInputField (1)/Text')
        sleep(10)
        self.tap('EmailAdvanceInputField (1)/Text')
        #wait time for keypad to load
        sleep(2)
        self.base_class.enter_text_app('EmailAdvanceInputField (1)/Text',email)
        self.altdriver.find_element('Window1/Save').tap()
        
    