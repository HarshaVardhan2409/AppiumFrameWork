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
        #wait for initial load of elements
        sleep(3.5)
        for row in self.table:
            #wait time for options to load
            #sleep(1)
            start_position = self.mcq.get_object_location(generics_lib.get_data(self.path, self.game_name, 'animation_object'))
            self.mcq.tap_option(row["option"])
            #wait time for animation to happen
            sleep(1.5)
            end_position = self.mcq.get_object_location(generics_lib.get_data(self.path, self.game_name, 'animation_object'))
            self.mcq.verify_object_location(start_position, end_position, row["acceptable"])
            