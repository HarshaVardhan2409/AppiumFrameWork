'''
This module contains tasks in Hangman scene
'''
import os
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
sys.path.append(PATH('../'))
from base_class import BaseClass

class Hangman(BaseClass):
    '''
    This class contains methods to perform actions on hangman template
    '''

    def tap_option(self, option):
        try:
            self.altdriver.wait_for_element_where_name_contains(option).mobile_tap()
        except:
            self.altdriver.wait_for_element_where_name_contains(option).tap()