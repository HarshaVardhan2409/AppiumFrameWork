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

class ParentGateway(GenericStep):
        
    @step('user taps on parent zone button in world map')
    def tap_on_parent_zone_button(self):
        self.execute_steps(u'''
        When tap on element: "ParentButton"
        ''')
        
    @step('parent gating screen should appear')
    def verify_parent_gate_panel(self):
        self.execute_steps(u'''
        Then verify the element:
            | object_name |
            | ParentGatePanel |
        ''')    
        
    @step('taps on right sided arrow the parent gating screen')
    def tap_on_close_arrow(self):
        self.base_class.get_object_name('Close')
        sleep(3)
        self.obj.altdriver.find_element_where_name_contains('Close').tap()    
        
    @step('answers the parent gating by typing in the text box')
    def enter_the_answer(self):
        self.execute_steps(u'''
        When parental access: "Question"
        ''')    
    
    @step('app should redirects user to parent zone landing screen')
    def verify_parent_zone_context(self):
        self.execute_steps(u'''
        Then verify the element:
            | object_name |
            | ParentZone |
        And custom wait: "3"
        ''')    
        
    @step('taps on refresh button')
    def tap_on_refresh_button(self):
        self.execute_steps(u'''
        When verify the element:
            | object_name |
            | Question |
        And tap on element: "Refresh question"
        And custom wait: "3"
        ''')    
        
    @step('app should refresh old security question with new one')
    def verify_new_question(self):
        self.execute_steps(u'''
        Then verify the element:
            | object_name |
            | Question |
        And custom wait: "3"
        ''')    
        
    @step('taps on add child')
    def tap_on_add_child_button(self):
        self.execute_steps(u'''
        Then verify the element:
            | object_name |
            | ParentZone |
        And tap on element: "AddProfileButton(Clone)"
        And verify the element:
            | object_name |
            | AddChildPanel(Clone)/Window1 |
        And custom wait: "3"
        ''') 
       
    @step('taps on child nickname place holder text and enters text')
    def tap_and_enter_child_nickname(self):
        self.execute_steps(u'''
        When tap on element: "Nickname-InputField/AdvInputField"
        And enter the: "Child's Nickname": "jhon" in element: "Nickname-InputField/AdvInputField"
        And custom wait: "3"
        ''')    
        
    @step('selects the grade')
    def select_the_grade(self):
        self.execute_steps(u'''
        Then tap on text element: "Text" with text: "Grade 3"
        And custom wait: "3"
        ''')    
        
    @step('taps on next button')
    def tap_on_next_button(self):
        self.execute_steps(u'''
        Then tap on element: "Next-Button"
        And verify the element:
            | object_name |
            | AddChildPanel(Clone)/Window2 |
        And custom wait: "3"
        ''')    
        
    @step('taps on lets begin button')
    def tap_on_lets_begin_button(self):
        self.execute_steps(u'''
        Then tap on element: "StartGame-Button"
        And verify the element:
            | object_name |
            | ProfilePanel/AvatarSelectionPanel |
        And custom wait: "3"
        ''')
        
    @step('select avatar picture')
    def select_avatar(self):
        self.execute_steps(u'''
        When select any avatar
        And custom wait: "3"
        ''')
        
            
    @step('taps on get set go')
    def select_letsgo(self):
        self.execute_steps(u'''
            When tap on element: "LetsStartButton"
            And scene is loaded: "GameMapScreen"
            And wait for object not to be present: "Interstitial"
            ''')
        
    @step('answers the parent gating by typing in the text box with wrong answer')
    def enter_wrong_answer(self):
        self.execute_steps(u'''
        When wrong parental access: "Question"
        ''')
        
    @step('answer field should be refreshed on tapping refresh button')
    def verify_answer_field(self):
        self.execute_steps(u'''
        Then verify the element:
            | object_name |
            | AnswerPanel |
        And custom wait: "3"
        ''')    
        
    @step('taps on right arrow/anywhere with in the parent gateway screen')
    def tap_on_anywhere(self):
        self.execute_steps(u'''
        Then tap on element: "ParentGate"
        ''')
        
    @step('parent gateway screen should be closed')
    def verify_parent_gateway_screen_closed(self):
        self.execute_steps(u'''
        Then scene is loaded: "GameMapScreen"
        ''')    
        
