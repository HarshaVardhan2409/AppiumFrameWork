import sys
from time import sleep

sys.path.append('../generics/')
import constants
import generics_lib

from ..games.templates.classification.classification import Classification
from generic_steps import GenericStep




class ClassificationStep(GenericStep):
    
    classify = None
    
    @when('drag and drop the draggables to bucket and verify position')
    def drag_and_drop_the_draggables_to_bucket(self):
        
        self.classify = Classification(self.obj.altdriver, self.obj.driver)
        
        for row in self.table:
            #wait time for elements to appear on the screen
            sleep(2)
            start_position = self.classify.get_object_location(row["draggable"])
            self.classify.drag_object_to_bucket(row['draggable'], row['bucket'])
            axis = generics_lib.get_data(self.path, self.game_name, 'axis')
            sleep(1)
            end_position = self.classify.get_object_location(row["draggable"])
            if 'x' in axis:
                self.classify.verify_object_location(start_position['x'], end_position['x'], row["acceptable"])
            elif 'y' in axis:
                self.classify.verify_object_location(start_position['y'], end_position['y'], row["acceptable"])
    
