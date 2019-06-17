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

