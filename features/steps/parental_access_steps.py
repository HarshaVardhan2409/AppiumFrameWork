from time import sleep
import sys
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../app/'))
from parental_access import ParentalAccess

sys.path.append(PATH('../../generics/'))
import constants
import generics_lib

sys.path.append(PATH('./'))
from generic_steps import GenericStep

class ParentAccessSteps(GenericStep):
    
    access = None
    
    @step('parental access: "{object_name}"')
    def parental_access(self, object_name):
        self.access = ParentalAccess(self.obj.altdriver, self.obj.driver)
        #wait for the question to load
        sleep(3)
        self.access.parental_access(object_name)