from time import sleep
import sys
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../app/'))
from parentzone import Parentzone

sys.path.append(PATH('../../generics/'))
import constants
import generics_lib

sys.path.append(PATH('./'))
from generic_steps import GenericStep
sys.path.append(PATH('../games/templates/'))
from base_class import BaseClass

class ParentZoneSteps(GenericStep):
    
    @step('select my account')
    def myaccount(self):
        self.parentzone = Parentzone(self.obj.altdriver, self.obj.driver)
        self.parentzone.myaccount()
        
    @step('select my child')
    def mychild(self):
        self.parentzone = Parentzone(self.obj.altdriver, self.obj.driver)
        self.parentzone.mychild()
        
    @step('select payment plans')
    def mypaymentplan(self):
        self.parentzone = Parentzone(self.obj.altdriver, self.obj.driver)
        self.parentzone.paymentplan()

    @step('click on terms of use')
    def click_on_terms_of_use(self):
        self.parentzone = Parentzone(self.obj.altdriver, self.obj.driver)
        self.parentzone.verify_others_section('Terms of use','Terms & Conditions')
        self.base_class.click_back()
        
    @step('click on Privacy Policy')
    def click_on_Privacy_Policy(self):
        self.parentzone = Parentzone(self.obj.altdriver, self.obj.driver)
        self.parentzone.verify_others_section('Privacy','Privacy Policy')
        self.base_class.click_back()
   
    @step('click on Rate us')
    def click_on_Rate_us(self):
        self.parentzone = Parentzone(self.obj.altdriver, self.obj.driver)
        #generics_lib.scroll(self.driver, 0.5, 0.5, 0.6, 0.1, 800)
        self.parentzone.verify_rate_us('rateUs')
        self.base_class.click_back()
      
    @step('change parent info "{parent_name}"')
    def change_parent_info(self,parent_name):
        self.parentzone = Parentzone(self.obj.altdriver, self.obj.driver)
        self.parentzone.change_parent_info(parent_name)  
        
    @step('click on Edit "{email}"')
    def account_details(self,email):
        self.parentzone = Parentzone(self.obj.altdriver, self.obj.driver)
        self.parentzone.account_details('Edit',email)
         
    @step('click on Logout')
    def click_on_Logout(self):
        self.parentzone = Parentzone(self.obj.altdriver, self.obj.driver)
        self.parentzone.click_on_logout()