'''
This module contains tasks in MCQ scene
'''
from ..base_class import BaseClass

class MCQ(BaseClass):
    '''
    This class contains methods to perform mcq actions
    '''

    def tap_option(self, option):
        self.altdriver.wait_for_element_where_name_contains(option).tap()