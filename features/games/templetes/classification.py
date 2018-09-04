'''
This module contains tasks in Scene Classification
'''
from time import sleep


class Classification():
    '''
    This class contains methods to perform classification
    '''
    altdriver = None
    driver = None


    def __init__(self, altdriver, driver):
        self.altdriver = altdriver
        self.driver = driver

    def click_classification(self):
        self.altdriver.wait_for_current_scene_to_be('LaunchPad')
        self.altdriver.wait_for_element('Button').tap()
        self.altdriver.wait_for_current_scene_to_be('classification')
        
    def verify_main_screen(self):
        self.altdriver.wait_for_current_scene_to_be('LaunchPad')
    
    def verify_classification_screen(self):
        self.altdriver.wait_for_current_scene_to_be('classification')

    def verify_the_elements_on_screen(self):
            self.altdriver.wait_for_current_scene_to_be('classification')
            self.altdriver.wait_for_element('Box')
            
    def drag_object(self, object_name):
        self.altdriver.wait_for_current_scene_to_be('classification')
        self.altdriver.wait_for_element_where_name_contains(object_name).dragToElement(
            self.altdriver.wait_for_element('Box')
            )
        
    def object_location_y(self, object):
        value = self.altdriver.wait_for_element_where_name_contains(object).y
        return value
    
    def object_name(self, object):
        value = self.altdriver.wait_for_element_where_name_contains(object).name
        return value
    
    def verify_question_1(self, object):
        name = Classification.object_name(self, object)
        assert 'Stage_1' in name
    
    def verify_question_2(self, object):
        sleep(6)
        name = Classification.object_name(self, object)
        assert 'Stage_2' in name