from time import sleep

from ..games.templates.mcq.mcq import MCQ
import sys

sys.path.append('../generics/')
import generics_lib
import constants

from generic_steps import GenericStep

class McqStep(GenericStep):
    
    mcq = None

    @when('select the option and verify')
    def select_the_option_and_verify(self):
        self.mcq = MCQ(self.obj.altdriver, self.obj.driver)
          
        for row in self.table:
            sleep(2)
            start_position = self.mcq.get_object_location(row["option"])
            self.mcq.tap_option(row["option"])
            axis = generics_lib.get_data(self.path, self.game_name, 'axis')
            sleep(1)
            end_position = self.mcq.get_object_location(row["option"])
            if 'x' in axis:
                self.mcq.verify_object_location(start_position['x'], end_position['x'], row["acceptable"])
            elif 'y' in axis:
                self.mcq.verify_object_location(start_position['y'], end_position['y'], row["acceptable"])
                
    @when('select the option')
    def select_the_option(self):
        self.mcq = MCQ(self.obj.altdriver, self.obj.driver)
        for row in self.table:
            sleep(3)
            self.mcq.tap_option(row["option"])
            
    @then('verify the level successful message')
    def verify_level_successful_message(self):
        for row in self.table:
            self.mcq.level_successful_message(row['object_name'], row['text'])