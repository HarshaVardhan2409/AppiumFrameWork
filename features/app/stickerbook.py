import os
import sys
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../games/templates/'))
from base_class import BaseClass

sys.path.append(PATH('../../generics'))
import generics_lib

class StickerBook(BaseClass):
    
    def stickerbook_draw(self, start_x, end_x, start_y, end_y):
        generics_lib.scroll(self.driver, start_x, end_x, start_y, end_y, 2600)
        
    def drag_object(self, draggable_name, nickName, end_x, end_y):
        self.altdriver.wait_for_element_where_name_contains(draggable_name).tap()
        elements = self.altdriver.find_elements(draggable_name)
        for i in range(len(elements)):
            name = elements[i].get_component_property('Byjus.K123.StickerBook', 'nickName')
            if nickName in name:
                elements[i].mobile_dragTo(end_x, end_y, 1200)
                break
                
        
        