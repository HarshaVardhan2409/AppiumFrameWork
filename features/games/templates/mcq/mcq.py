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

    def level_successful_message(self, object_name, expected_text):
        actual_text = self.altdriver.wait_for_element_where_name_contains(object_name).get_text()
        assert expected_text in actual_text

