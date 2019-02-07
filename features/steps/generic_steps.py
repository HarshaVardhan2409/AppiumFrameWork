from time import sleep
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
        
    @step('GameMapScreen is loaded with test credentials: "{number}"')
    def gamemapscreen_testcredentials(self, number):
        self.path = PATH('../../config/config.json')
        try:
            self.obj.launch_app(generics_lib.get_data(self.path, 'app_config', "app_package"), generics_lib.get_data(self.path, 'app_config', "app_activity"), 'True')
            print '1st'
            self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
            self.base_class.verify_scene('GameMapScreen')
            self.base_class.wait_for_element_not_present('Interstitial')
            self.base_class.verify_scene('GameMapScreen')
            self.base_class.verify_text_for_duplicate_objects('Text', 'utomation')
        except:
            print '3rd'
            try:
                self.obj.teardown()
            except:
                print 'not launched'
            print '4th'
            self.execute_steps(u'''
            Given launch the app
            Given scene is loaded: "OnboardingIntroScene"
            When tap on element: "Button"
            Then scene is loaded: "Onboarding"
            When custom wait: "3"
            And tap on element: "MobilePanel/InputFieldPrefab"
            And tap on element with text: "NONE OF THE ABOVE"
            ''')
            self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
            self.base_class.enter_text_app('MobilePanel/InputFieldPrefab', number)
            self.execute_steps(u'''
            When tap on element: "NextButton"
            Then verify the element:
            | object_name            |
            | OTPVerification(Clone) |
            When enter the: "otp": "1234" in element: "InputFieldPrefab"
            And scene is loaded: "GameMapScreen"
            And wait for object not to be present: "Interstitial"
            And scene is loaded: "GameMapScreen"
            And verify text lines in multiple text boxes for object with same names:
            | object_name | text |
            | Text | utomation |
            ''')
            
    @step('GameMapScreen scene is loaded')
    def gamemap_scene_loaded(self):
        self.path = PATH('../../config/config.json')
        try:
            self.obj.launch_app(generics_lib.get_data(self.path, 'app_config', "app_package"), generics_lib.get_data(self.path, 'app_config', "app_activity"), 'True')
            print '1st'
            self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
            self.base_class.verify_scene('GameMapScreen')
            self.base_class.wait_for_element_not_present('Interstitial')
            print '2nd'
        except:
            print '3rd'
            try:
                self.obj.teardown()
            except:
                print 'not launched'
            print '4th'
            self.execute_steps(u'''
            Given launch the app
            Given scene is loaded: "OnboardingIntroScene"
            When tap on element: "Button"
            Then scene is loaded: "Onboarding"
            When custom wait: "3"
            And tap on element: "MobilePanel/InputFieldPrefab"
            And tap on element with text: "NONE OF THE ABOVE"
            And enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
            And tap on element: "NextButton"
            And enter the: "nick name": "jimmy" in element: "GradeSelection(Clone)/Background/InputFieldPrefab"
            And tap on text element: "Text" with text: "Grade 3"
            And tap on element: "NextButton"
            Then verify the element:
            | object_name            |
            | OTPVerification(Clone) |
            When enter the: "otp": "1234" in element: "InputFieldPrefab"
            Then verify the element:
            | object_name             |
            | LocationAndEmail(Clone) |
            And tap on element: "LocationPanel/InputField"
            And tap on element: "LocateMeButton"
            And tap on element with text: "Allow"
            And tap on element: "EmailPanel/InputFieldPrefab"
            And tap on element with text: "@"
            And tap on element with text: "OK"
            And tap on element: "NextButton"
            Then verify the element:
            | object_name                |
            | OnBoardingCompleted(Clone) |
            And custom wait: "3"
            And tap on element: "NextButton"
            Then scene is loaded: "GameMapScreen"
            And wait for object not to be present: "Interstitial"
            And tap on element: "Avatar(Clone)"
            And tap on element: "LetsStartButton"
            And scene is loaded: "GameMapScreen"
            ''')
        
    @step('stickerbook scene is loaded')
    def sticker_scene_loaded(self):
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        self.base_class.tap('Stickerbook')
        self.base_class.wait_for_scene('stickerbook')
        self.base_class.wait_for_element_not_present('Interstitial')
        self.base_class.wait_for_element_display('final-page')
        sleep(4)
               
    @step('Library scene is loaded')
    def library_scene_loaded(self):    
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        self.base_class.tap('LibraryButton')
        self.access = ParentalAccess(self.obj.altdriver, self.obj.driver)
        #wait for the question to load
        sleep(3)
        self.access.parental_access('ParentGatePanel/Question')
        self.base_class.wait_for_scene('Library')
        self.base_class.wait_for_element_not_present('Interstitial')
        
    @step('ParentZone scene is loaded')
    def ParentZone_scene_loaded(self):
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        self.base_class.tap('ParentButton/FillImage')
        self.access = ParentalAccess(self.obj.altdriver, self.obj.driver)
        #wait for the question to load
        sleep(3)
        self.access.parental_access('ParentGatePanel/Question')
        self.base_class.wait_for_scene('ParentZone')
        self.base_class.wait_for_element_not_present('Interstitial')
        
    @step('question is loaded')
    def question_is_loaded(self):
        #for row in self.table:
            #self.base_class.wait_for_element_display(row["object_name"])
            #break
        for row in self.table:
            self.base_class.verify_question(row["object_name"])
                
    @step('wait for object not to be present: "{object_name}"')
    def object_not_present(self, object_name):
        self.base_class.wait_for_element_not_present(object_name)
            
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
            
    @step('verify the text associated with component of the elements')
    def verify_text_for_the_component(self):
        for row in self.table:
            self.base_class.verify_text_of_component(str(row['component_name']),str(row['component_property']),str(row['object_name']), str(row['text']))     
            
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

    '''
    object which does not contain on_Click() method, the below step should be used
    '''
    @step('tap on element location: "{object_name}"')
    def mobiletap(self, object_name):
        self.base_class.mobiletap(object_name)

    @step('tap and hold element: "{object_name}" for duration: "{duration}"')
    def tap_and_hold(self, object_name, duration):
        self.base_class.tap_and_hold(object_name, duration)

    @step('tap on the element: "{object_name}" with component property title: "{title}"')
    def tap_on_title(self, object_name, title):
        self.base_class.tap_title(object_name, title)
    
        
    @step('enter the: "{name}": "{text}" in element: "{object_name}"')
    def enter_text(self, name, text, object_name):
        if "mobile number" in name:
            self.base_class.tap(object_name)
            try:
                self.base_class.tap_element_text(text)
            except:
                print 'SIM not available'
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
        if "NONE OF" in text:
            try:
                self.base_class.tap_element_text(text)
            except:
                print 'SIM not available'
        else:
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
        
    @step('verify orientation is portrait')
    def verify_orientation_potrait(self):
        self.base_class.verify_orientation('portrait')
        
    @step('verify orientation is landscape')
    def verify_orientation_landscape(self):
        self.base_class.verify_orientation('landscape')

    @step('verify the element on screen')
    def verfiy_element_on_load(self):
        for row in self.table:
            self.base_class.wait_for_element_display(row['object_name'])  
            
    @step('press device home button')
    def press_home_button(self):
        self.base_class.home_button()
        
    @step('select the game: "{text}" with element: "{object_name}"')
    def verify_element_games(self, text, object_name):
        self.base_class.select_game(text, object_name)
        
    @step('draw on sticker book from start_x: "{start_xvalue}" end_x: "{end_xvalue}" start_y: "{start_yvalue}" end_y: "{end_yvalue}"')
    def stickerbook_draw(self, start_xvalue, end_xvalue, start_yvalue, end_yvalue):
        self.base_class.draw(float(start_xvalue), float(end_xvalue), float(start_yvalue), float(end_yvalue))


