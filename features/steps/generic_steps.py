from time import sleep
import sys
from behave import *

sys.path.append('../features/')
from games.templates.base_class import BaseClass

sys.path.append('../generics/')
import generics_lib
import constants
import test_management

class GenericStep():
    
    start_position = None
    end_position = None
    game_name = None
    
    base_class = None
    path = None
    
    case = None
    run = None
    
    @step('game is launched with text')
    def game_is_launched_with_text(self):
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        
        for row in self.table:
            self.game_name = row["game_name"]
            
        if 'classification' in self.game_name:
            self.path = constants.classification_path
        elif 'mcq' in self.game_name:
            self.path = constants.mcq_path
            
        text_field = generics_lib.get_data(self.path, self.game_name, "text_field")
        game_code = generics_lib.get_data(self.path, self.game_name, "game_code")
        load_button = generics_lib.get_data(self.path, self.game_name, "load_game")
        
        self.base_class.wait_for_scene(generics_lib.get_data(self.path, self.game_name, "launch_screen"))
        self.base_class.start_game_with_text(text_field, game_code, load_button)
    
    @step('game is launched')
    def game_is_launched(self):
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        
        for row in self.table:
            self.game_name = row["game_name"]
            
        if 'classification' in self.game_name:
            self.path = constants.classification_path
        elif 'mcq' in self.game_name:
            self.path = constants.mcq_path
            
        self.base_class.wait_for_scene(generics_lib.get_data(self.path, self.game_name, "launch_screen"))
        self.base_class.start_game(generics_lib.get_data(self.path, self.game_name, "launch_game"))
        
    
    @step('start scene is loaded')
    def start_scene_is_loaded(self):
        self.base_class.wait_for_scene(generics_lib.get_data(self.path, self.game_name, "start_screen"))
    
    @step('question is loaded')
    def question_is_loaded(self):
        for row in self.table:
            self.base_class.verify_question(row["object_with_question"], row["question_number"])
            self.base_class.wait_for_element_display(row["question_number"])
            
    @step('verify the level successful message')
    def verify_level_successful_message(self):
        for row in self.table:
            self.base_class.level_successful_message(row['object_name'], row['text'])
            
    @step('verify the text')
    def verify_the_text(self):
        for row in self.table:
            self.base_class.verify_text(row['object_name'], generics_lib.get_data(self.path, self.game_name, "text"))
            
            
    @then('update the result to testrail: case {caseID} : suite {runID}')
    def update_result_to_testrail(self, caseID, runID):
        print ''
            