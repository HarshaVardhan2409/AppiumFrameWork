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
        
    def drag_object_and_verify(self, draggable_name, nickName, end_x, end_y):
        dSize = (self.driver.get_window_size())
        end_x = (dSize['width']*end_x)
        end_y = (dSize['height']*end_y)
        self.altdriver.wait_for_element_where_name_contains(draggable_name).tap()
        elements = self.altdriver.find_elements(draggable_name)
        for i in range(len(elements)):
            name = elements[i].get_component_property('Byjus.K123.StickerBook.StickerView', 'nickName')
            if nickName in name:
                sleep(1)
                print 'mobile drag to'
                elements[i].mobile_dragTo(end_x, end_y, 6000)
                break
        sleep(1)
        draggable_nickname = ''
        dragabbles = self.altdriver.find_elements('DraggableStickerPrefab(Clone)')
        for i in range(len(dragabbles)):
            if nickName in dragabbles[i].get_component_property('Byjus.K123.StickerBook.DraggableStickerView', 'nickName'):
                #dragabbles[i].mobile_dragTo(end_x, end_y, 3000)
                draggable_nickname = dragabbles[i].get_component_property('Byjus.K123.StickerBook.DraggableStickerView', 'nickName')
                print draggable_nickname
                break
        assert nickName in draggable_nickname
                
    def delete_object_and_verify(self, draggable_name, nickName):
        self.altdriver.wait_for_element_where_name_contains(draggable_name).tap()
        elements = self.altdriver.find_elements(draggable_name)
        for i in range(len(elements)):
            name = elements[i].get_component_property('Byjus.K123.StickerBook.DraggableStickerView', 'nickName')
            if nickName in name:
                sleep(1)
                elements[i].mobile_tap(2)
                delete_button = self.altdriver.find_element('DeleteButton')
                x = delete_button.x
                y = delete_button.mobileY
                elements[i].mobile_dragTo(x, y, 3000)
        
        