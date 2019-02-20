'''
This module contains tasks in MCQ scene
'''
import os
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
sys.path.append(PATH('../'))
from base_class import BaseClass

class MCQ(BaseClass):
    '''
    This class contains methods to perform actions on mcq template
    '''

    def tap_option(self, option):
        try:
            self.altdriver.wait_for_element(option).mobile_tap()
        except:
            self.altdriver.wait_for_element(option).tap()