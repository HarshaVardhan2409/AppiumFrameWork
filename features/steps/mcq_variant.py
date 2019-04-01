from time import sleep
import sys
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../games/templates/'))
from mcq.mcq import MCQ

sys.path.append(PATH('../../generics/'))
import constants
import generics_lib

sys.path.append(PATH('./'))
from generic_steps import GenericStep

class McqStep(GenericStep):
    
    mcq = None
    
    @step('select the option and verify')
    def select_the_option_and_verify(self):
        for row in self.table:
            self.base_class.wait_for_element_display(row['option'])
            break
        self.mcq = MCQ(self.obj.altdriver, self.obj.driver)
        #wait for initial load of elements
        sleep(4)
        for row in self.table:
            #wait time for options to load
            start_position = self.mcq.get_object_location(row['animation_object'])
            self.mcq.tap_option(row["option"])
            if 'rue' in row["option"]:
                sleep(6)
            else:
                sleep(4)
            end_position = self.mcq.get_object_location(row['animation_object'])
            self.mcq.verify_object_location(start_position, end_position, row["acceptable"])


