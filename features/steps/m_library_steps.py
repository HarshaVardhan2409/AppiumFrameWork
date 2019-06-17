from time import sleep
from ast import literal_eval
import sys
from behave import *
import random
import subprocess
import os
from behave.textutil import text
from behave.runner import Context

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


sys.path.append(PATH('../'))
from base_setup import BaseSetup

sys.path.append(PATH('../games/templates/'))
from base_class import BaseClass

sys.path.append(PATH('./'))
from generic_steps import GenericStep

sys.path.append(PATH('../../generics/'))
import generics_lib
import constants
import test_management

class LibrarySteps(GenericStep):
    
    @step('adding videos to favourite')
    def adding_videos_to_favourite(self): 
        for row in self.table:
            #self.base_class.wait_for_element_display(row['object_name'])  
            self.base_class.adding_video_to_favourite(row['video_name'])
        
    @step('verify favorites tab')
    def verify_favourites_tab(self): 
        for row in self.table:
            self.base_class.verify_favorites(row['video_name'])
            
    @step('switch child profile "{profile_name}"')
    def switch_child_profile(self,profile_name):
        self.base_class.switch_profiles(profile_name)
        
    @step('select grade number "{grade_name}"')
    def select_grade_number(self,grade_name):
        self.execute_steps(u'''
              When ParentZone scene is loaded
             ''')  
        sleep(5)
        self.base_class.switch_grade(grade_name)
        self.execute_steps(u'''
              When scene is loaded: "GameMapScreen"
             ''')
    @step('select child profile "{profile_name}"')
    def select_child_profile(self,profile_name):
        self.base_class.wait_for_scene('ProfileSelectionScene')
        self.base_class.select_profiles(profile_name)  
        
    @step('verify count of video "{video_name}"')
    def verify_count_of_video(self,video_name):
        self.base_class.verify_countOf_videos(video_name)
        
    @step('select the chapter in library: "{chap_name}"') 
    def select_the_chapter(self,chap_name):
        self.execute_steps(u'''
        When select the game: "{chap_name}" with element: "Header"
        '''.format(chap_name=chap_name))
        
    @step('select the tab in library: "{tab_name}"') 
    def select_the_tab(self,tab_name):
        self.execute_steps(u'''
        When tap on text element: "Text" with text: "{tab_name}"
        '''.format(tab_name=tab_name))
        