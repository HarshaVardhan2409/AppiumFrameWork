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

sys.path.append(PATH('../app/'))
from quests import Quests

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
        self.quest = Quests(self.obj.altdriver, self.obj.driver)
        self.execute_steps(u'''
            When Onboarding scene is loaded
            When custom wait: "3"
            And tap on element with text: "NONE OF THE ABOVE"
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
        self.quest = Quests(self.obj.altdriver, self.obj.driver)
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
        self.quest = Quests(self.obj.altdriver, self.obj.driver)
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
        self.quest = Quests(self.obj.altdriver, self.obj.driver)
        self.quest.check_avatar_selected('Tick', 'true')
        
    @step('tap on different avatar other than selected avatar')
    def select_diff_avatar(self):
        self.quest = Quests(self.obj.altdriver, self.obj.driver)
        self.quest.select_avatar('Avatar(Clone)', 'piglet')
        
    @step('whole screen should be greyed out')
    def whole_screen_grey(self):
        self.quest = Quests(self.obj.altdriver, self.obj.driver)
        self.quest.check_avatar_highlighted('Avatar(Clone)', 'pooh')
        
    @step('previously selected avatar should get dehighlighted')
    def diff_avatar(self):
        self.quest = Quests(self.obj.altdriver, self.obj.driver)
        self.quest.check_avatar_highlighted('Avatar(Clone)', 'piglet')

