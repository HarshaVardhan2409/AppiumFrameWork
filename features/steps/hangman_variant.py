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
        check = ''
        flag = False
        self.hangman = Hangman(self.obj.altdriver, self.obj.driver)
        for row in self.table:
            self.base_class.wait_for_element_display(row['option'])
            try:
                check = str(self.obj.altdriver.wait_for_element(row['option']).get_component_property('Byjus.K123.Templates.MCQ.GameElement', 'interactive'))
                count = 0
                while check.lower() == 'false' and count < 30:
                    sleep(1)
                    check = str(self.obj.altdriver.wait_for_element(row['option']).get_component_property('Byjus.K123.Templates.MCQ.GameElement', 'interactive'))
                    count += 1
            except:
                print ''
            break
        sleep(5)
        for row in self.table:
            ''' for MCQ waiting '''
            try:
                val_mcq = 0
                check = str(self.obj.altdriver.wait_for_element(row['option']).get_component_property('Byjus.K123.Templates.MCQ.GameElement', 'interactive'))
                while check.lower() == 'true' and val_mcq < 30:
                    sleep(1)
                    print 'tapping mcq........................'
                    self.hangman.tap_option(row['option'])
                    sleep(0.5)
                    check = str(self.obj.altdriver.wait_for_element(row['option']).get_component_property('Byjus.K123.Templates.MCQ.GameElement', 'interactive'))
                    val_mcq += 1
                assert check == 'false', 'Unable to select option'    
            except:
                print ''
            
            ''' for hangman waiting '''
            try:
                val_hangman = 0
                check = str(self.obj.altdriver.find_element(row['option']).get_component_property('Byjus.K123.Templates.Hangman.HMOptionsView', 'disable'))
                answer = str(self.obj.altdriver.find_element(row['option']).get_component_property('Byjus.K123.Templates.Hangman.HMOptionsView', 'answered'))
                while (check.lower() == 'false' and answer.lower() == 'false') and val_hangman < 30:
                    sleep(1)
                    print 'tapping hangman........................'
                    self.hangman.tap_option(row['option'])
                    sleep(0.5)
                    check = str(self.obj.altdriver.find_element(row['option']).get_component_property('Byjus.K123.Templates.Hangman.HMOptionsView', 'disable'))
                    answer = str(self.obj.altdriver.find_element(row['option']).get_component_property('Byjus.K123.Templates.Hangman.HMOptionsView', 'answered'))
                    val_hangman += 1
                assert check == 'true', 'Unable to select option'
            except:
                print ''
                
    @step('select the correct and incorrect option')
    def select_correct_incorrect_option(self):
        check = ''
        flag = False
        self.hangman = Hangman(self.obj.altdriver, self.obj.driver)
        for row in self.table:
            self.base_class.wait_for_element_display(row['option'])
            try:
                check = str(self.obj.altdriver.wait_for_element(row['option']).get_component_property('Byjus.K123.Templates.MCQ.GameElement', 'interactive'))
                count = 0
                while check.lower() == 'false' and count < 30:
                    sleep(1)
                    check = str(self.obj.altdriver.wait_for_element(row['option']).get_component_property('Byjus.K123.Templates.MCQ.GameElement', 'interactive'))
                    count += 1
            except:
                print ''
            break
        sleep(5)
        for row in self.table:
            ''' for MCQ waiting '''
            if row['acceptable'] == 'true':
                try:
                    val_mcq = 0
                    check = str(self.obj.altdriver.wait_for_element(row['option']).get_component_property('Byjus.K123.Templates.MCQ.GameElement', 'interactive'))
                    while check.lower() == 'true' and val_mcq < 30:
                        sleep(1)
                        print 'tapping mcq........................'
                        self.hangman.tap_option(row['option'])
                        sleep(0.5)
                        check = str(self.obj.altdriver.wait_for_element(row['option']).get_component_property('Byjus.K123.Templates.MCQ.GameElement', 'interactive'))
                        val_mcq += 1
                    assert check == 'false', 'Unable to select option'    
                except:
                    print ''
                
                ''' for hangman waiting '''
                try:
                    val_hangman = 0
                    check = str(self.obj.altdriver.find_element(row['option']).get_component_property('Byjus.K123.Templates.Hangman.HMOptionsView', 'disable'))
                    answer = str(self.obj.altdriver.find_element(row['option']).get_component_property('Byjus.K123.Templates.Hangman.HMOptionsView', 'answered'))
                    while (check.lower() == 'false' and answer.lower() == 'false') and val_hangman < 30:
                        sleep(1)
                        print 'tapping hangman........................'
                        self.hangman.tap_option(row['option'])
                        sleep(0.5)
                        check = str(self.obj.altdriver.find_element(row['option']).get_component_property('Byjus.K123.Templates.Hangman.HMOptionsView', 'disable'))
                        answer = str(self.obj.altdriver.find_element(row['option']).get_component_property('Byjus.K123.Templates.Hangman.HMOptionsView', 'answered'))
                        val_hangman += 1
                    assert check == 'true', 'Unable to select option'
                except:
                    print ''
            elif row['acceptable'] == 'false':
                try:
                    val_mcq = 0
                    check = str(self.obj.altdriver.wait_for_element(row['option']).get_component_property('Byjus.K123.Templates.MCQ.GameElement', 'interactive'))
                    while check.lower() == 'true' and val_mcq < 2:
                        sleep(2)
                        print 'tapping mcq........................'
                        self.hangman.tap_option(row['option'])
                        sleep(0.5)
                        check = str(self.obj.altdriver.wait_for_element(row['option']).get_component_property('Byjus.K123.Templates.MCQ.GameElement', 'interactive'))
                        val_mcq += 1
                    assert check == 'true', 'Unable to select option'    
                except:
                    print ''
                
                ''' for hangman waiting '''
                try:
                    val_hangman = 0
                    check = str(self.obj.altdriver.find_element(row['option']).get_component_property('Byjus.K123.Templates.Hangman.HMOptionsView', 'disable'))
                    answer = str(self.obj.altdriver.find_element(row['option']).get_component_property('Byjus.K123.Templates.Hangman.HMOptionsView', 'answered'))
                    while (check.lower() == 'false' and answer.lower() == 'false') and val_hangman < 2:
                        sleep(2)
                        print 'tapping hangman........................'
                        self.hangman.tap_option(row['option'])
                        sleep(0.5)
                        check = str(self.obj.altdriver.find_element(row['option']).get_component_property('Byjus.K123.Templates.Hangman.HMOptionsView', 'disable'))
                        answer = str(self.obj.altdriver.find_element(row['option']).get_component_property('Byjus.K123.Templates.Hangman.HMOptionsView', 'answered'))
                        val_hangman += 1
                    assert check.lower() == 'false' and answer.lower() == 'false', 'Unable to select option'
                except:
                    print ''
                    
