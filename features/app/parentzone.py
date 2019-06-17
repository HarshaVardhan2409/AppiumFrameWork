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
    
    