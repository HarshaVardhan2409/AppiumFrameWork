import sys
from time import sleep
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../../generics/'))
import constants
import generics_lib

sys.path.append(PATH('../games/templates/'))
from classification.classification import Classification

sys.path.append(PATH('./'))
from generic_steps import GenericStep

class ClassificationStep(GenericStep):
    
    classification = None
    
    @step('drag and drop the draggables to bucket and verify position')
    def drag_and_drop_the_draggables_to_bucket(self):
        for row in self.table:
            self.base_class.wait_for_element_display(row['draggable'])
            break
        self.classification = Classification(self.obj.altdriver, self.obj.driver)
        #wait time for elemnts to be loaded
        sleep(3.5)
        for row in self.table:
            #wait time for elements to appear on the screen
            sleep(1)
            start_position = self.classification.get_object_location(row["draggable"])
            #self.classification.drag_object_to_bucket(row['draggable'], row['bucket'])
            self.base_class.multiple_drag_and_drop(row['draggable'],row['bucket'])
            #wait time for animation to happen
            sleep(2)
            end_position = self.classification.get_object_location(row["draggable"])
            self.classification.verify_object_location(start_position, end_position, row["acceptable"])
    
    @step('multiple drag and drop: "{option_1}" "{option_2}" "{option_3}"')
    def select_multiple_options(self,option_1,option_2,option_3):
        self.base_class.multiple_drag_and_drop(option_1,option_2,option_3)

