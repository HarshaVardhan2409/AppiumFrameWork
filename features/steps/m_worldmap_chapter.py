from time import sleep
from ast import literal_eval
import sys
from behave import *
import random
import subprocess
import os
from behave.textutil import text
from behave.runner import Context
from appium.webdriver.common.touch_action import TouchAction

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../'))
from base_setup import BaseSetup

sys.path.append(PATH('../games/templates/'))
from base_class import BaseClass

sys.path.append(PATH('../app/'))
from buildings import Buildings

sys.path.append(PATH('./'))
from generic_steps import GenericStep

sys.path.append(PATH('../../generics/'))
import generics_lib
import constants
import test_management

class WorldMapChapters(GenericStep):

    quest = None

    @step('user completes the account creation process till avatar selection')
    def account_creation(self):
        self.quest = Buildings(self.obj.altdriver, self.obj.driver)
        self.execute_steps(u'''
            When Onboarding scene is loaded
            When custom wait: "3"
            And tap on element with text: "None of the above"
            And enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
            And tap on element: "Toggler"
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
            Given scene is loaded: "GameMapScreen"
            And wait for object not to be present: "Interstitial"
            And custom wait: "3"
            ''')

    @step('user should be on world map screen')
    def worldmap_screen(self):
        self.execute_steps(u'''
            Given scene is loaded: "GameMapScreen"
            And wait for object not to be present: "Interstitial"
            And custom wait: "3"
            ''')

    @step('user should not be able to dismiss the avatar screen by tapping on any area of the black overlay')
    @step('avatar selection screen should appear on top of that')
    def avtar_screen(self):
        self.execute_steps(u'''
            Then verify the element:
            | object_name |
            | Avatar(Clone) |
            ''')

    @step('avatar selection screen should not appear for already login user')
    def avatar_not_present(self):
        self.execute_steps(u'''
            Then wait for object not to be present: "Avatar(Clone)"
            ''')
        
    @step('tap again on selected avatar')
    @step('select any avatar')
    def select_avatar(self):
        self.quest = Buildings(self.obj.altdriver, self.obj.driver)
        self.quest.select_avatar('Avatar(Clone)', 'pooh')

    @step('tap on "Get Set Go" button')
    def select_letsgo(self):
        self.execute_steps(u'''
            When tap on element: "LetsStartButton"
            ''')

    @step('user should be able to proceed to world map after selecting the avatar and after tapping "Get Set Go" button')
    def selecting_avatar(self):
        self.execute_steps(u'''
            Then avatar selection screen should not appear for already login user
            ''')

    @step('no avatar should be selected by default')
    def avatar_not_selected(self):
        self.quest = Buildings(self.obj.altdriver, self.obj.driver)
        self.quest.check_avatar_selected('Tick', 'false')


    @step('"Get Set Go" button should not be present')
    def letsgo_not_enabled(self):
        self.execute_steps(u'''
            Then wait for object not to be present: "LetsStartButton"
            ''')

    @step('"Get Set Go" button should be highlighted')
    def letsgo_enabled(self):
        self.execute_steps(u'''
            Then verify the element:
            | object_name |
            | LetsStartButton |
            ''')

    @step('user should not be able to deselect the selected avatar')
    @step('user selected avatar should be highlighted with green color tick')
    def avatar_selected(self):
        self.quest = Buildings(self.obj.altdriver, self.obj.driver)
        self.quest.check_avatar_selected('Tick', 'true')
        
    @step('tap on different avatar other than selected avatar')
    def select_diff_avatar(self):
        self.quest = Buildings(self.obj.altdriver, self.obj.driver)
        self.quest.select_avatar('Avatar(Clone)', 'piglet')
        
    @step('whole screen should be greyed out')
    def whole_screen_grey(self):
        self.quest = Buildings(self.obj.altdriver, self.obj.driver)
        self.quest.check_avatar_highlighted('Avatar(Clone)', 'pooh')
        
    @step('previously selected avatar should get dehighlighted')
    def diff_avatar(self):
        self.quest = Buildings(self.obj.altdriver, self.obj.driver)
        self.quest.check_avatar_highlighted('Avatar(Clone)', 'piglet')

    @step('tap on any area of the black overlay')
    def tap_on_background(self):
        action = TouchAction(self.obj.driver)
        dSize = (self.obj.driver.get_window_size())
        x = (dSize['width']*0.5)
        y = (dSize['height']*0.1)
        action.tap(x=x, y=y)
        
    @step('user kills app')
    def kill_app(self):
        self.execute_steps(u'''
            When close the app
            ''')

    @step('user relaunches app')
    def relaunch_app(self):
        self.execute_steps(u'''
            When launch app with apppackage: "com.byjus.k3" appactivity: "com.byjus.unity.support.activities.MainActivity"
            ''')
        
    @step('screen title should be "Hey xxxx, pick your favourite"')
    def verify_title(self):
        self.execute_steps(u'''
            Then verify the text: "Hey Jimmy, pick your favourite" for element: "AvatarBoothPanel/Title"
            ''')

    @step('user puts the app on resents and relaunches')
    def recent_apps(self):
        self.execute_steps(u'''
            When put the app on background
            ''')

    @step('user goes to home screen')
    def press_home_button(self):
        self.obj.driver.press_keycode(3)

    @step('user relaunches app from background')
    def relaunch_background(self):
        self.obj.driver.activate_app('com.byjus.k3')
        
    @step('user should be able to see following attributes in chapter screen : Profile Selection icon, Chapter List, Sticker book icon, Library icon, Parent Zone icon')
    def verify_worldmap_elements(self):
        self.execute_steps(u'''
            Then verify the element:
            | object_name |
            | ProfileIcon |
            | Buildings   |
            | Stickerbook |
            | LibraryButton |
            | ParentButton |
            ''')
    @step('user swipes horizontally to left or right on chapter list')
    def swipe_chapter_screen(self):
        self.execute_steps(u'''
        When scroll screen with start_x: "0.9" end_x: "0.1" start_y: "0.5" end_y: "0.5" and verify element: "Building_1(Clone)"
        ''')
        
    @step('app should show all the chapters available in that grade')
    def verify_chapters(self):
        self.execute_steps(u'''
            Then verify the element:
            | object_name |
            | Building_1(Clone) |
            | Building_2(Clone) |
            | Building_3(Clone) |
            | Building_4(Clone) |
            ''')

    @step('app should switch from portrait to landscape mode')
    def landscape_on_gamemapscreen(self):
        self.execute_steps(u'''
        Then scene is loaded: "GameMapScreen"
        And wait for object not to be present: "Interstitial"
        And verify orientation is landscape
        ''')
        
    @step('app should show a black overlay screen')
    @step('app should open profile selection screen on top of that')
    def profile_screen(self):
        self.execute_steps(u'''
            Then verify the element:
            | object_name |
            | Building_1(Clone) |
            | ProfileContext(Clone) |
            ''')
    @step('user taps on profile icon')
    def tap_profile(self):
        self.execute_steps(u'''
            When tap on element: "ProfileIcon/Frame"
            ''')
    
    