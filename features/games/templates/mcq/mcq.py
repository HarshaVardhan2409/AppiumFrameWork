'''
This module contains tasks in MCQ scene
'''
from ..base_class import BaseClass

class MCQ(BaseClass):
    '''
    This class contains methods to perform mcq actions
    '''

    def verify_main_screen(self):
        self.altdriver.wait_for_current_scene_to_be('LaunchPad')
    
    def verify_mcq_screen(self):
        self.altdriver.wait_for_current_scene_to_be('MCQ')
        
    def verify_question_1(self):
        self.altdriver.wait_for_current_scene_to_be('MCQ')
        try:
            self.altdriver.wait_for_element_where_name_contains('stage_001')
        except:
            self.altdriver.wait_for_element_where_name_contains('mcq_four')
        name = self.altdriver.wait_for_element_where_name_contains('mcq_four').name
        name = str(name)
        assert 'stage_001' in name
        
    def verify_question_2(self):
        self.altdriver.wait_for_current_scene_to_be('MCQ')
        try:
            self.altdriver.wait_for_element_where_name_contains('stage_002')
        except:
            self.altdriver.wait_for_element_where_name_contains('mcq_four')
        name = self.altdriver.wait_for_element_where_name_contains('mcq_four').name
        name = str(name)
        assert 'stage_002' in name
        
    def verify_question_3(self):
        self.altdriver.wait_for_current_scene_to_be('MCQ')
        try:
            self.altdriver.wait_for_element_where_name_contains('stage_003')
        except:
            self.altdriver.wait_for_element_where_name_contains('mcq_four')
        name = self.altdriver.wait_for_element_where_name_contains('mcq_four').name
        name = str(name)
        assert 'stage_003' in name
        
    def click_mcq(self):
        self.altdriver.wait_for_current_scene_to_be('LaunchPad')
        self.altdriver.wait_for_element('MCQ').tap()

    def tap_option(self, option):
        self.altdriver.wait_for_element(option).tap()
        
    def check_animation(self, option):
        value = self.altdriver.wait_for_element(option).x
        print type(value)
        print value
        
    def verify_popup(self, popup):
        text = self.altdriver.wait_for_element_where_name_contains('GratificationText').get_text()
        assert popup in text
        
        