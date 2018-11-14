'''
This module contains tasks in Scene Classification
'''
import os
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
sys.path.append(PATH('../'))
from base_class import BaseClass

class Classification(BaseClass):
    '''
    This class contains methods to perform actions on classification template
    '''
            
    def drag_object_to_bucket(self, draggable_name, bucket_name):
        self.altdriver.wait_for_element_where_name_contains(draggable_name).tap()
        self.altdriver.wait_for_element_where_name_contains(draggable_name).dragToElement(
            self.altdriver.wait_for_element_where_name_contains(bucket_name)
            )