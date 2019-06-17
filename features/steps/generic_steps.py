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
    
    @step('launch app with apppackage: "{appPackage}" appactivity: "{appActivity}" with no reset: "{status}"')
    def launch_app_activity_status(self, appPackage, appActivity, status):
        self.obj.launch_app(appPackage, appActivity, status)
       
    @step('relaunch the app')
    def relaunch(self):
        self.obj.launch_app("com.byjus.k3", "com.byjus.unity.support.activities.MainActivity", 'True')
        
    @step('put the app in background and launch')
    def background_app(self):
        self.obj.driver.background_app(5)
        sleep(2)

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
        self.base_class.wait_for_scene('Onboarding')
        self.base_class.tap('Button')
  
    @step('GameMapScreen is loaded with test credentials: "{number}" "{version}"')
    def gamemapscreen_testcredentials_version(self, number,version):
        self.obj.launch_app()
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        try:
            print "entered try"
            self.base_class.verify_scene('Loading')
            self.base_class.verify_the_element_on_screen('loadingbg/Canvas/Text')
            versi1=self.base_class.get_text('loadingbg/Canvas/Text')
            print "entered app and checking version"
            print version
            assert str(versi1) in str(version)
            self.base_class.verify_scene('GameMapScreen')
            self.base_class.wait_for_element_not_present('Interstitial/FadeTransition-Loading')
            self.base_class.verify_scene('GameMapScreen')
        except:
            print "entered except"
            self.base_class.wait_for_scene('Onboarding')
            try:
                self.base_class.tap('Button')
                self.execute_steps(u'''
                When custom wait: "3"
                And tap on element with text: "None of the above"
                ''')
            except:
                self.execute_steps(u'''
                When custom wait: "3"
                And tap on element with text: "None of the above"
                ''')

            self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
            self.base_class.tap('MobilePanel/InputFieldPrefab')
            sleep(0.5)
            self.base_class.clear_text('MobilePanel/InputFieldPrefab/Text')
            sleep(1)
            self.base_class.enter_text_app('MobilePanel/InputFieldPrefab', number)
            self.execute_steps(u'''
            When tap on element: "Toggler"
            And tap on element: "NextButton"
            Then verify the element:
                | object_name            |
               | OTPVerification(Clone) |
            When enter the: "otp": "1234" in element: "InputFieldPrefab"
            And custom wait: "3"
            ''')
            self.base_class.verify_scene('GameMapScreen')
            self.base_class.wait_for_element_not_present('Interstitial')
            self.base_class.verify_scene('GameMapScreen')
            
            self.execute_steps(u'''
            Given ParentZone scene is loaded
            ''')
            sleep(3)
            versi1=self.base_class.get_text('VersionNumber')
            print "entered app and checking version"
            print version
            assert str(versi1) in str(version)
            self.base_class.tap('BackButton')
            sleep(8)
            
    @step('GameMapScreen is loaded with test credentials: "{number}"')
    def gamemapscreen_testcredentials(self, number):
        self.obj.launch_app()
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        current_scene = self.obj.altdriver.get_current_scene()
        while str(current_scene) == 'Loading':
            sleep(1)
            current_scene = self.obj.altdriver.get_current_scene()
        current_scene = self.obj.altdriver.get_current_scene()
        if 'GameMapScreen' == str(current_scene):
            print "entered gamemapscreen condition"
            self.base_class.verify_scene('GameMapScreen')
            self.base_class.wait_for_element_not_present('Interstitial/FadeTransition-Loading')
            sleep(5)
        elif 'Onboarding' == str(current_scene):
            print "entered onboarding condition"
            self.base_class.wait_for_scene('Onboarding')
            try:
                self.obj.altdriver.wait_for_element('Button', timeout=10)
                self.base_class.tap('Button')
                self.execute_steps(u'''
                When custom wait: "3"
                And tap on element with text: "None of the above"
                ''')
            except:
                self.execute_steps(u'''
                When custom wait: "3"
                And tap on element with text: "None of the above"
                ''')
            self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
            self.base_class.tap('MobilePanel/InputFieldPrefab')
            sleep(0.5)
            self.base_class.clear_text('MobilePanel/InputFieldPrefab/Text')
            sleep(1)
            self.base_class.enter_text_app('MobilePanel/InputFieldPrefab', number)
            self.execute_steps(u'''
            When tap on element: "Toggler"
            And tap on element: "NextButton"
            Then verify the element:
                | object_name            |
               | OTPVerification(Clone) |
            When enter the: "otp": "1234" in element: "InputFieldPrefab"
            And scene is loaded: "GameMapScreen"
            And wait for object not to be present: "Interstitial/FadeTransition-Loading"
            And custom wait: "5"
            ''')
            
    @step('GameMapScreen is loaded')
    def gamemap_scene_loaded(self):
        self.obj.install_app()
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        current_scene = self.obj.altdriver.get_current_scene()
        while str(current_scene) == 'Loading':
            sleep(1)
            current_scene = self.obj.altdriver.get_current_scene()
        current_scene = self.obj.altdriver.get_current_scene()
        if 'GameMapScreen' == str(current_scene):
            print "entered gamemapscreen condition"
            self.base_class.verify_scene('GameMapScreen')
            self.base_class.wait_for_element_not_present('Interstitial/FadeTransition-Loading')
            sleep(5)
        elif 'Onboarding' == str(current_scene):
            print "entered onboarding condition"
            self.base_class.wait_for_scene('Onboarding')
            try:
                self.obj.altdriver.wait_for_element('Button', timeout=10)
                self.base_class.tap('Button')
                self.execute_steps(u'''
                When custom wait: "3"
                And tap on element with text: "None of the above"
                ''')
            except:
                self.execute_steps(u'''
                When custom wait: "3"
                And tap on element with text: "None of the above"
                ''')
            self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
            self.base_class.tap('MobilePanel/InputFieldPrefab')
            sleep(0.5)
            self.base_class.clear_text('MobilePanel/InputFieldPrefab/Text')
            sleep(1)
            self.execute_steps(u'''
            When enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
            And tap on element: "Toggler"
            And tap on element: "NextButton"
            And enter the: "nick name": "jimmy" in element: "GradeSelection(Clone)/Background/InputFieldPrefab"
            And tap on text element: "Text" with text: "Class 2"
            And tap on element: "NextButton"
            Then verify the element:
            | object_name            |
            | OTPVerification(Clone) |
            When enter the: "otp": "1234" in element: "InputFieldPrefab"
            Then verify the element:
            | object_name             |
            | LocationAndEmail(Clone) |
            And tap on element: "LocationDetector/InputField"
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
            And wait for object not to be present: "Interstitial/FadeTransition-Loading"
            And tap on element: "Avatar(Clone)"
            And tap on element: "LetsStartButton"
            And scene is loaded: "GameMapScreen"
            And custom wait: "3"
            ''')
        
    @step('stickerbook scene is loaded')
    def sticker_scene_loaded(self):
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        self.base_class.tap('Stickerbook')
        self.base_class.wait_for_scene('stickerbook')
        self.base_class.wait_for_element_not_present('Interstitial/FadeTransition-Loading')
        self.base_class.wait_for_element_display('grade3-frozen')
        sleep(4)
               
    @step('Library scene is loaded')
    def library_scene_loaded(self):    
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        self.base_class.tap('LibraryButton')
        self.access = ParentalAccess(self.obj.altdriver, self.obj.driver)
        #wait for the question to load
        sleep(3)
        self.access.parental_access('ParentGatePanel/AnswerPanel/Question')
        self.base_class.wait_for_scene('Library')
        self.base_class.wait_for_element_not_present('Interstitial/FadeTransition-Loading')
        
    @step('parentzone scene is loaded')
    def ParentZone_scene_loaded(self):
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
        self.base_class.tap('ParentButton/FillImage')
        self.access = ParentalAccess(self.obj.altdriver, self.obj.driver)
        #wait for the question to load
        sleep(3)
        self.access.parental_access('ParentGatePanel/AnswerPanel/Question')
        self.base_class.wait_for_scene('ParentZone')
        self.base_class.wait_for_element_not_present('Interstitial/FadeTransition-Loading')
        sleep(2)
        
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
        self.base_class = BaseClass(self.obj.altdriver, self.obj.driver)
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
            subprocess.Popen('adb logcat | findstr ' + str(package_name) + ' > ' + constants.PATH('../execution_data/app_logs/logs_caseID_' + data[1] + '_runID_' + data[0] + '.json'), shell=True)
        except:
            subprocess.Popen('adb logcat | grep ' + str(package_name) + ' > ' + constants.PATH('../execution_data/app_logs/logs_caseID_' + data[1] + '_runID_' + data[0] + '.json'), shell=True)

    @step('tap on element: "{object_name}"')
    def tap(self, object_name):
        self.base_class.tap(object_name)

    '''
    object which does not contain on_Click() method, the below step should be used
    '''
    @step('tap on element location: "{object_name}"')
    def mobiletap(self, object_name):
        self.base_class.mobiletap(object_name)
    
    @step('offline tap on image "{image_name}"')
    def image_tap(self, image_name):
        self.base_class.tap_image(image_name)
        
    @step('offline verify image "{image_name}"')
    def verify_image(self, image_name):
        self.base_class.verify_image(image_name)
    
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
        if "None of the" in text:
            try:
                self.base_class.tap("InputFieldPrefab/Text")
                try:
                    self.base_class.tap_element_text(text)
                except:
                    self.base_class.tap_element_text(text.upper())        
                self.obj.driver.implicitly_wait(20)
            except:
                self.obj.driver.implicitly_wait(20)
            print 'SIM not available'
        elif "Allow" in text:
            try:
                self.base_class.tap_element_text(text)
            except:
                self.base_class.tap_element_text(text.upper())        
            self.obj.driver.implicitly_wait(20)
        else:
            self.base_class.tap_element_text(text)
        
    @step('custom wait: "{time}"')
    def wait(self, time):
        sleep(int(time))
        
    @step('scroll screen with start_x: "{start_xvalue}" end_x: "{end_xvalue}" start_y: "{start_yvalue}" end_y: "{end_yvalue}" and verify element: "{object_name}"')
    def scrollverify(self, start_xvalue, end_xvalue, start_yvalue, end_yvalue, object_name):
        self.base_class.scroll_verify(object_name, float(start_xvalue), float(end_xvalue), float(start_yvalue), float(end_yvalue))
        
    @step('scroll screen with start_x: "{start_xvalue}" end_x: "{end_xvalue}" start_y: "{start_yvalue}" end_y: "{end_yvalue}" and verify element: "{object_name}" for no movement')
    def scrollverifymovement(self, start_xvalue, end_xvalue, start_yvalue, end_yvalue, object_name):
        self.base_class.scroll_verify_for_false(object_name, float(start_xvalue), float(end_xvalue), float(start_yvalue), float(end_yvalue))
        
    @step('scroll screen with start_x: "{start_xvalue}" end_x: "{end_xvalue}" start_y: "{start_yvalue}" end_y: "{end_yvalue}"')
    def scroll(self, start_xvalue, end_xvalue, start_yvalue, end_yvalue):
        self.base_class.scroll(float(start_xvalue), float(end_xvalue), float(start_yvalue), float(end_yvalue))
        
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
        
    @step('put the app on background')
    def put_app_on_background(self):
        self.base_class.put_app_background()
        
    @step('select the game: "{text}" with element: "{object_name}"')
    def verify_element_games(self, text, object_name):
        self.base_class.select_game(text, object_name)
        
    @step('uninstall the app')
    def uninstall_app(self):
        self.obj.driver.remove_app('com.byjus.k3')


    @step('verify hint') 
    def verfiy_hint(self):
        try:
            for row in self.table:
                self.base_class.verify_presence_of_hint(row['object_name'])
        except:
            self.execute_steps(u'''
              Then verify HintBulb content
             ''')  
      
            
    @step('verify HintBulb content') 
    def verfiy_hint_content(self):
        self.execute_steps(u'''
        When verify the element:
            | object_name |
            | HintBulbImage |
        And tap on element: "HintBulbImage"
        ''')
        try:
            self.execute_steps(u'''
            And verify the element:
                | object_name |
                | HintPanel |
                | HintImage |
            And tap on element: "CloseButton"
            ''')
        except:
            print "Hint image without popup"
            
    @step('verify HintBulb content "{img_name}"') 
    def verfiy_hint_content1(self,img_name):
        self.execute_steps(u'''
        When verify the element:
            | object_name |
            | HintBulbImage |
        And tap on element: "HintBulbImage"
        And verify the element:
            | object_name |
            | HintPanel |
            | HintImage |
        And pixel comparision of images for "{img_name}"
        And tap on element: "CloseButton"
        '''.format(img_name=img_name))
            
    @step('pixel comparision of images for "{image_name}"')
    def pixel_comparision(self, image_name):
        generics_lib.takescreenshot(self.obj.driver, PATH('../../a_image/actual_'+image_name+'_pixel.png'))
        generics_lib.pixel_comparision(PATH('../../a_image/'+image_name+'_pixel.png'), PATH('../../a_image/actual_'+image_name+'_pixel.png'))
    

    @step('color comparision of images for "{image_name}"')
    def color_comparision(self, image_name):
        generics_lib.takescreenshot(self.obj.driver, PATH('../../a_image/actual_'+image_name+'_color.png'))
        generics_lib.color_comparision(PATH('../../a_image/'+image_name+'_color.png'), PATH('../../a_image/actual_'+image_name+'_color.png'))

