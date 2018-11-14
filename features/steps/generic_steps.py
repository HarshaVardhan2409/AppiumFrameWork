from time import sleep
import sys
from behave import *
import subprocess
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../games/templates/'))
from base_class import BaseClass

sys.path.append(PATH('../../generics/'))
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
        
    @step('game is launched with text and url')
    def game_is_launched_with_text_url(self):
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        
        for row in self.table:
            self.game_name = row["game_name"]
            
        if 'classification' in self.game_name:
            self.path = constants.classification_path
        elif 'mcq' in self.game_name:
            self.path = constants.mcq_path
            
        text_field = generics_lib.get_data(self.path, self.game_name, "text_field")
        text = generics_lib.get_data(self.path, self.game_name, "template_name")
        url_field = generics_lib.get_data(self.path, self.game_name, "url_field")
        bundle_url = generics_lib.get_data(self.path, self.game_name, "bundle_url")
        load_button = generics_lib.get_data(self.path, self.game_name, "load_game")
        
        self.base_class.wait_for_scene(generics_lib.get_data(self.path, self.game_name, "launch_screen"))
        self.base_class.start_game_with_text_url(text_field, text, url_field, bundle_url, load_button)
    
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
            self.base_class.verify_question(row["object_name"])
            self.base_class.wait_for_element_display(row["object_name"])
            
    @step('verify the text: "{expected_text}" for element: "{element_name}"')
    def verify_the_text(self, element_name, expected_text):
        self.base_class.verify_text(str(element_name), str(expected_text))
            
    @step('verify text lines in multiple text boxes')
    def verify_the_multiple_texts(self):
        for row in self.table:
            self.base_class.verify_text(row['object_name'], row['text'])
            
    @step('verify the element')
    def verify_element(self):
            for row in self.table:
                self.base_class.verify_the_element_on_screen(row['object_name'])
            
    @step('capture the app logs for: "{package_name}"')
    def capture_logs(self, package_name):
        data = None
        data = str(self.scenario)
        data = data.split('">')
        data = data[0].split('_')
        data.reverse()
        subprocess.Popen('adb logcat -c', shell=True)
        try:
            subprocess.Popen('adb logcat | findstr ' + str(package_name) + ' > ' + constants.PATH('../execution_data/app_logs/logs_caseID_' + data[1] + '_runID_' + data[0] + '.txt'), shell=True)
        except:
            subprocess.Popen('adb logcat | grep ' + str(package_name) + ' > ' + constants.PATH('../execution_data/app_logs/logs_caseID_' + data[1] + '_runID_' + data[0] + '.txt'), shell=True)
        
    @step('tap on element: "{object_name}"')
    def tap(self, object_name):
        self.base_class.tap(object_name)


    @step('tap and hold element: "{object_name}" for duration: {duration}')
    def tap_and_hold(self, object_name, duration):
        self.base_class.tap_and_hold(object_name, duration)
        
    @step('enter the: "{name}": "{text}" in element: "{object_name}"')
    def enter_text(self, name, text, object_name):
        self.base_class.enter_text_app(object_name, text)
        
    @then('update the result to testrail')
    def update_result_to_testrail(self):
        print ''