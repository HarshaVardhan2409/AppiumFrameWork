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

class InstallationOnboarding(GenericStep):
    
    screen_location_start = None
    screen_location_end = None
    screen_location_start2 = None
    screen_location_end2 = None
    
    
    @step('install the app and launch online')
    def install_and_launch_app(self):
        self.execute_steps(u'''
        Given launch the app
        ''')
        
    @step('user is not logged in')
    def not_logged_in(self):
        self.execute_steps(u'''
        Given scene is loaded: "Onboarding"
        And custom wait: "3"
        ''')
        
    @step('user is logged in')
    def looged_in(self):
        self.execute_steps(u'''
        Given Onboarding scene is loaded
        When custom wait: "3"
        And tap on element with text: "NONE OF THE ABOVE"
        And enter the: "number": "4444555502" in element: "MobilePanel/InputFieldPrefab"
        And tap on element: "Toggler"
        And tap on element: "NextButton"
        Then verify the element:
        | object_name            |
        | OTPVerification(Clone) |
        When enter the: "otp": "1234" in element: "InputFieldPrefab"
        Then scene is loaded: "GameMapScreen"
        And wait for object not to be present: "Interstitial"
        And custom wait: "3"
        ''')
        
    @step('install the app and logged in')
    def logged_in(self):
        self.execute_steps(u'''
        Given GameMapScreen is loaded with test credentials: "4444555502"
        ''')
        
    @step('taps on get started button')
    def logged_in(self):
        self.execute_steps(u'''
        When Onboarding scene is loaded
        ''')
    
    @step('user enters an existing mobile number')
    def enter_existing_number(self):
        self.execute_steps(u'''
        When tap on element with text: "NONE OF THE ABOVE"
        And enter the: "test number": "4444555502" in element: "MobilePanel/InputFieldPrefab"
        And tap on element: "Toggler"
        And tap on element: "NextButton"
        ''')
        
    @step('user enters a new mobile number')
    def enter_new_number(self):
        self.execute_steps(u'''
        Given tap on element with text: "NONE OF THE ABOVE"
        And enter the: "different mobile number": "4444555502" in element: "MobilePanel/InputFieldPrefab"
        And tap on element: "Toggler"
        And tap on element: "NextButton"
        ''')
        
    @step('user enters the respective otp or otp is auto verified')
    def enter_otp(self):
        self.execute_steps(u'''
        Then verify the element:
        | object_name            |
        | OTPVerification(Clone) |
        And enter the: "otp": "1234" in element: "InputFieldPrefab"
        ''')
        
    @step('app switches from portrait to landscape mode on reaching onboarding')
    def portrait_on_onboarding(self):
        self.execute_steps(u'''
        Then scene is loaded: "Onboarding"
        And verify orientation is portrait
        ''')

    @step('app switches from portrait to landscape mode on reaching account creation')
    def portrait_on_account(self):
        self.execute_steps(u'''
        Then scene is loaded: "Onboarding"
        And verify orientation is portrait
        ''')

    @step('app switches from Portrait to landscape mode on reaching World Map')
    def landscape_on_gamemapscreen(self):
        self.execute_steps(u'''
        Then scene is loaded: "GameMapScreen"
        And wait for object not to be present: "Interstitial"
        And verify orientation is landscape
        ''')

    @step('enter the child name and select the grade 3')
    def child_name_and_grade(self):
        self.execute_steps(u'''
        When scene is loaded: "Onboarding"
        And custom wait: "3"
        And enter the: "nick name": "jimmy" in element: "GradeSelection(Clone)/Background/InputFieldPrefab"
        And tap on text element: "Text" with text: "Grade 3"
        And tap on element: "NextButton"
        ''')
        
    @step('enter the location and email')
    def enter_location_email(self):
        self.execute_steps(u'''
        When verify the element:
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
        ''')
        
    @step('user restarts the app')
    def restart_app(self):
        self.execute_steps(u'''
        When launch app with apppackage: "com.byjus.k3" appactivity: "com.byjus.unity.support.activities.MainActivity"
        And scene is loaded: "Onboarding"
        ''')
    
    @step('user kills the app on splash screen')
    def kill_app(self):
        self.execute_steps(u'''
        When close the app
        ''')
        
    @step('restart the app with data cleared')
    def restart_app_cleared(self):
        self.execute_steps(u'''
        When launch app with apppackage: "com.byjus.k3" appactivity: "com.byjus.unity.support.activities.MainActivity" with no reset: "False"
        ''')
    
    
    @step('user is on account creation screen')
    def account_creation_screen(self):
        self.execute_steps(u'''
        Then verify the element:
        | object_name  |
        | MobilePanel |
        ''')
    
    @step('user is on onboarding screen')
    def onboarding_screen(self):
        self.execute_steps(u'''
        Then scene is loaded: "Onboarding"
        Then verify the element:
        | object_name  |
        | Button |
        ''')

    @step('user uninstalls the app')
    def uninstall_app(self):
        self.execute_steps(u'''
        When uninstall the app
        ''')

    @step('performs a left or right swipe')
    def swipe_action(self):
        self.screen_location_start = self.base_class.get_object_location('Content')
        self.execute_steps(u'''
        When scroll screen with start_x: "0.9" end_x: "0.1" start_y: "0.5" end_y: "0.5"
        And scroll screen with start_x: "0.9" end_x: "0.1" start_y: "0.5" end_y: "0.5"
        ''')
    
    @step('the screens should scroll accordingly')
    def check_scroll(self):
        self.screen_location_end = self.base_class.get_object_location('Content')
        self.base_class.verify_object_location(self.screen_location_start, self.screen_location_end, 'true')
        
    @step('scrolls the three screens')
    def scroll_three_screens(self):
        self.screen_location_start = self.base_class.get_object_location('SlidePrefab(Clone)')
        self.execute_steps(u'''
        When scroll screen with start_x: "0.9" end_x: "0.1" start_y: "0.5" end_y: "0.5"
        And scroll screen with start_x: "0.9" end_x: "0.1" start_y: "0.5" end_y: "0.5"
        And scroll screen with start_x: "0.9" end_x: "0.1" start_y: "0.5" end_y: "0.5"
        ''')

    @step('only three scrollable screens should be present in on-boarding screen')
    def check_for_three_screens(self):
        self.screen_location_end = self.base_class.get_object_location('SlidePrefab(Clone)')
        self.base_class.verify_object_location(self.screen_location_start, self.screen_location_end, 'true')

    @step('scrolls right in the third screen')
    def swipe_right_third_screen(self):
        self.screen_location_start = self.base_class.get_object_location('SlidePrefab(Clone)')
        self.execute_steps(u'''
        When scroll screen with start_x: "0.9" end_x: "0.1" start_y: "0.5" end_y: "0.5"
        And scroll screen with start_x: "0.9" end_x: "0.1" start_y: "0.5" end_y: "0.5"
        And scroll screen with start_x: "0.9" end_x: "0.1" start_y: "0.5" end_y: "0.5"
        And scroll screen with start_x: "0.9" end_x: "0.1" start_y: "0.5" end_y: "0.5"
        ''')

    @step('then scrolls left in the first screen')
    def swipe_left_first_screen(self):
        value = literal_eval(self.base_class.get_component_property('SlidePrefab(Clone)', "UnityEngine.RectTransform", "localRotation"))
        self.screen_location_start2 = {'x': value[0], 'y': value[1]}
        self.execute_steps(u'''
        When scroll screen with start_x: "0.1" end_x: "0.9" start_y: "0.5" end_y: "0.5"
        And scroll screen with start_x: "0.1" end_x: "0.9" start_y: "0.5" end_y: "0.5"
        And scroll screen with start_x: "0.1" end_x: "0.9" start_y: "0.5" end_y: "0.5"
        And scroll screen with start_x: "0.1" end_x: "0.9" start_y: "0.5" end_y: "0.5"
        ''')
        value = literal_eval(self.base_class.get_component_property('SlidePrefab(Clone)', "UnityEngine.RectTransform", "localRotation"))
        self.screen_location_end2 = {'x': value[0], 'y': value[1]}

    @step('screen 3 should slide to 1 but screen 1 should not slide to screen 3')
    def verify_three_screens(self):
        self.screen_location_end = self.base_class.get_object_location('SlidePrefab(Clone)')
        print '------------------------'
        print self.screen_location_start2
        print self.screen_location_end2
        print type(self.screen_location_start2)
        print type(self.screen_location_end2)
        self.base_class.verify_object_location(self.screen_location_start, self.screen_location_end, 'true')
        self.base_class.verify_object_location(self.screen_location_start2, self.screen_location_end2, 'false')


    @step('leave app idle until it auto scrolls to screen 3')
    def app_idle(self):
        sleep(8)
        
    @step("user doesn't interact with a screen for 4 seconds")
    def screen_idle(self):
        self.screen_location_start = self.base_class.get_object_location('Content')
        sleep(4)
        self.screen_location_end = self.base_class.get_object_location('Content')
        
    @step('next onboarding screen should be scrolled to automatically')
    def next_onboarding_screen(self):
        self.base_class.verify_object_location(self.screen_location_start, self.screen_location_end, 'true')
