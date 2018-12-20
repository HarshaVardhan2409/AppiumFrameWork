from time import sleep
import sys
from behave import *
import random
import subprocess
import os
from behave.textutil import text

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../app/'))
from parental_access import ParentalAccess

sys.path.append(PATH('../'))
from base_setup import BaseSetup

sys.path.append(PATH('../games/templates/'))
from base_class import BaseClass

sys.path.append(PATH('../../generics/'))
import generics_lib
import constants
import test_management

class GenericStep():
    obj = BaseSetup()
    start_position = None
    end_position = None
    game_name = None
    old = None
    base_class = None
    path = None
    
    case = None
    run = None
    '''    
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
    '''    
    
       
    @step('launch app with apppackage: "{appPackage}" appactivity: "{appActivity}"')
    def launch_app_activity(self, appPackage, appActivity):
        self.obj.launch_app(appPackage, appActivity, 'True')
        
    @step('launch the app')
    def launch_app(self):
        self.obj.install_app()
        
    @step('close the app')
    def close_app(self):
        self.obj.teardown()
        
    @step('scene is loaded: "{scene_name}"')
    def scene_loaded(self, scene_name):
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        self.base_class.wait_for_scene(scene_name)
        
    @step('Onboarding scene is loaded')
    def onboarding_scene_loaded(self):
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        self.base_class.wait_for_scene('OnboardingIntroScene')
        self.base_class.tap('Button')
        self.base_class.wait_for_scene('Onboarding')
        
    @step('GameMapScreen scene is loaded')
    def gamemap_scene_loaded(self):
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        self.base_class.wait_for_scene('GameMapScreen')
        
    @step('Library scene is loaded')
    def library_scene_loaded(self):
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        self.base_class.tap_and_hold('LibraryButton', 7)
        self.access = ParentalAccess(self.obj.altdriver, self.obj.driver)
        #wait for the question to load
        sleep(3)
        self.access.parental_access('ParentGatePanel/Question')
        self.base_class.wait_for_scene('Library')
        
    @step('question is loaded: "{object_name}"')
    def question_is_loaded(self, object_name):
            self.base_class.verify_question(object_name)
            self.base_class.wait_for_element_display(object_name)
            
    @step('verify the text: "{expected_text}" for element: "{element_name}"')
    def verify_the_text(self, element_name, expected_text):
        self.base_class.verify_text(str(element_name), str(expected_text))
            
    @step('verify text lines in multiple text boxes')
    def verify_the_multiple_texts(self):
        for row in self.table:
            self.base_class.verify_text(str(row['object_name']), str(row['text']))
            
    @step('verify text lines in multiple text boxes for object with same names')
    def verify_text_for_same_name_objects(self):
        for row in self.table:
            self.base_class.verify_text_for_duplicate_objects(str(row['object_name']), str(row['text']))
            
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


    @step('tap and hold element: "{object_name}" for duration: "{duration}"')
    def tap_and_hold(self, object_name, duration):
        self.base_class.tap_and_hold(object_name, duration)
        
    @step('enter the: "{name}": "{text}" in element: "{object_name}"')
    def enter_text(self, name, text, object_name):
        if "mobile number" in name:
            text = str(random.randint(1000000000,9999999999))
            if 'different' in name:
                text = str(random.randint(1000000000,9999999999))
                self.old = text
            elif 'same' in name:
                text = self.old
        self.base_class.enter_text_app(object_name, text)
        
    @step('clear text field: "{object_name}"')
    def clear_text(self, object_name):
        self.base_class.clear_text(object_name)
        
    @step('tap on text element: "{object_name}" with text: "{text}"')
    def text_tap(self, object_name, text):
        self.base_class.text_tap(object_name, text)
        
    @step('tap on element with text: "{text}"')
    def tap_element_text(self, text):
        self.base_class.tap_element_text(text)
        
    @step('custom wait: "{time}"')
    def wait(self, time):
        sleep(int(time))
        
    @step('scroll screen with start_x: "{start_xvalue}" end_x: "{end_xvalue}" start_y: "{start_yvalue}" end_y: "{end_yvalue}" and verify element: "{object_name}"')
    def scroll(self, start_xvalue, end_xvalue, start_yvalue, end_yvalue, object_name):
        self.base_class.scroll_verify(object_name, float(start_xvalue), float(end_xvalue), float(start_yvalue), float(end_yvalue))
        
    @step('verify native app for "{text}"')
    def verify_native_text(self, text):
        self.base_class.verify_native_text(text)
        
    @step('navigate back')
    def navigate_back(self):
        self.base_class.click_back()
        
    
    @then('update the result to testrail')
    def update_result_to_testrail(self):
        print ''
        