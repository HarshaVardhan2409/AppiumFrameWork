from time import sleep
import sys
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../games/templates/'))
from hangman.hangman import Hangman

sys.path.append(PATH('../../generics/'))
import constants
import generics_lib

sys.path.append(PATH('./'))
from generic_steps import GenericStep

class HangmanStep(GenericStep):
    
    hangman = None
    
    @step('select option and verify')
    def select_the_option_and_verify(self):
        for row in self.table:
            self.base_class.wait_for_element_display(row['option'])
            break
        self.hangman = Hangman(self.obj.altdriver, self.obj.driver)
        #wait for initial load of elements
        sleep(3.5)
        for row in self.table:
            #wait time for options to load
            sleep(1)
            start_position = self.hangman.get_object_location(row['animation_object'])
            self.hangman.tap_option(row['option'])
            #wait time for animation to happen
            sleep(3)
            end_position = self.hangman.get_object_location(row['animation_object'])
            self.hangman.verify_object_location(start_position, end_position, row['acceptable'])
            
    @step('choose the option and verify')
    def choose_the_option_and_verify(self):
        for row in self.table:
            self.base_class.wait_for_element_display(row['option'])
            break
        sleep(5)
        self.hangman = Hangman(self.obj.altdriver, self.obj.driver)
        start_position = None
        end_position = None
        #wait for initial load of elements
        
        for row in self.table:
            sleep(1)
            start_position = self.hangman.get_object_location(row['animation_object'])
        for row in self.table:
            #wait time for options to load
            
            self.hangman.tap_option(row['option'])
            #sleep(5)
        for row in self.table:
            #wait time for animation to happen
            end_position = self.hangman.get_object_location(row['animation_object'])
            break
        self.hangman.verify_object_location(start_position, end_position, row['acceptable'])
        
    @step('choose the valid option and verify')
    def choose_the_valid_option_and_verify(self):
        for row in self.table:
            self.base_class.wait_for_element_display(row['option'])
            break
        sleep(5)
        self.hangman = Hangman(self.obj.altdriver, self.obj.driver)
        start_position = None
        end_position = None
        #wait for initial load of elements
        
        for row in self.table:
            sleep(1)
            start_position = self.hangman.get_object_location(row['animation_object'])
        for row in self.table:
            #wait time for options to load
            
            self.hangman.tap_option(row['option'])
            sleep(2)
        for row in self.table:
            #wait time for animation to happen
            end_position = self.hangman.get_object_location(row['animation_object'])
            break
        self.hangman.verify_object_location(start_position, end_position, row['acceptable'])
        
    @step('select the option')
    def select_the_option(self):
        for row in self.table:
            self.base_class.wait_for_element_display(row['option'])
            break
        sleep(5)
        self.hangman = Hangman(self.obj.altdriver, self.obj.driver)
        for row in self.table:
            #wait time for options to load
            self.hangman.tap_option(row['option'])
            sleep(1)
