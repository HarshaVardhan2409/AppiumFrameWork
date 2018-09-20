'''
This module contains tasks in Scene Classification
'''
from ..base_class import BaseClass

class Classification(BaseClass):
    '''
    This class contains methods to perform classification
    '''
            
    def drag_object_to_bucket(self, draggable_name, bucket_name):
        self.altdriver.wait_for_element_where_name_contains(draggable_name).tap()
        self.altdriver.wait_for_element_where_name_contains(draggable_name).tap()
        self.altdriver.wait_for_element_where_name_contains(draggable_name).dragToElement(
            self.altdriver.wait_for_element_where_name_contains(bucket_name)
            )