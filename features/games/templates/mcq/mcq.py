'''
This module contains tasks in MCQ scene
'''
from ..base_class import BaseClass

class MCQ(BaseClass):
    '''
    This class contains methods to perform mcq actions
    '''

    def tap_option(self, option):
        self.altdriver.wait_for_element(option).tap()

    def check_animation(self, option):
        value = self.altdriver.wait_for_element(option).x
        print type(value)
        print value

    def verify_popup(self, popup):
        text = self.altdriver.wait_for_element_where_name_contains('GratificationText').get_text()
        assert popup in text

