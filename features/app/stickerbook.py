import os
import sys
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

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
            name = elements[i].get_component_property('Byjus.K123.StickerBook.StickerView', 'nickname')
            if nickName in name:
                sleep(1)
                print 'mobile drag to'
                elements[i].mobile_dragTo(end_x, end_y, 6000)
                break
        sleep(1)
        draggable_nickname = ''
        dragabbles = self.altdriver.find_elements('DraggableStickerPrefab(Clone)')
        for i in range(len(dragabbles)):
            if nickName in dragabbles[i].get_component_property('Byjus.K123.StickerBook.DraggableStickerView', 'stickerNickname'):
                #dragabbles[i].mobile_dragTo(end_x, end_y, 3000)
                draggable_nickname = dragabbles[i].get_component_property('Byjus.K123.StickerBook.DraggableStickerView', 'stickerNickname')
                print draggable_nickname
                break
        assert nickName in draggable_nickname
                
    def delete_object_and_verify(self, draggable_name, nickName):
        self.altdriver.wait_for_element_where_name_contains(draggable_name).tap()
        elements = self.altdriver.find_elements(draggable_name)
        for i in range(len(elements)):
            name = elements[i].get_component_property('Byjus.K123.StickerBook.DraggableStickerView', 'stickerNickname')
            if nickName in name:
                sleep(1)
                elements[i].mobile_tap(2)
                delete_button = self.altdriver.find_element('DeleteButton')
                x = delete_button.x
                y = delete_button.mobileY
                elements[i].mobile_dragTo(x, y, 3000)
        
    def check_sticker(self, sticker_name):
        start_name = '1'
        end_name = '2'
        name = ''
        count = 0
        flag = False
        elements = []
        action = TouchAction(self.driver)
        dSize = (self.driver.get_window_size())
        x = (dSize['width']*0.8)
        y = (dSize['height']*0.2)
        action.tap(x = x, y = y).perform()
        while start_name != end_name and count < 15:
            self.tap('OpenStickers')
            sleep(1)
            try:
                elements = self.altdriver.find_elements('StickerPrefab(Clone)')
            except: 
                print 'No stickers present..........'
            for i in range(len(elements)):
                if count == 0:
                    start_name = elements[0].get_component_property('Byjus.K123.StickerBook.StickerView', 'nickname')
                name = elements[i].get_component_property('Byjus.K123.StickerBook.StickerView', 'nickname')
                if count != 0:
                    end_name = elements[0].get_component_property('Byjus.K123.StickerBook.StickerView', 'nickname')
                if str(sticker_name) == str(name):
                    flag = True
                    break
            if flag == True:
                break
            for i in range(len(elements)):
                count += 1
                break
        assert name == sticker_name, 'Unable to find the sticker '+sticker_name

    def drag_stickers_from_category(self, sticker_name):
        flag = True
        count = 0
        while flag == True and count < 20:
            count += 1
            stickers = self.altdriver.find_elements_where_name_contains('grade')
            for sticker in stickers:
                if sticker_name in sticker.name:
                    sticker_name = str(sticker.name) + '/border image'
                    name = self.altdriver.find_element(sticker_name).get_component_property('UnityEngine.UI.Image', 'sprite')
                    count = 0
                    while 'ip_primary_border' not in name and count < 5:
                        count += 1 
                        self.tap('OpenStickers')
                        sleep(4)
                        name = self.altdriver.find_element(sticker_name).get_component_property('UnityEngine.UI.Image', 'sprite')
                    flag = False
                    break
            if flag == True:
                self.tap('OpenStickers')
                sleep(4)
        assert flag == False, 'Unable to find the stickers category with name '+ sticker_name
        dSize = (self.driver.get_window_size())
        end_x = (dSize['width']*0.25)
        end_y = (dSize['height']*0.5)
        self.altdriver.wait_for_element_where_name_contains('StickerPrefab(Clone)').tap()
        elements = self.altdriver.find_elements('StickerPrefab(Clone)')
        name = elements[0].get_component_property('Byjus.K123.StickerBook.StickerView', 'nickname')
        sleep(1)
        print 'mobile drag to'
        elements[0].mobile_dragTo(end_x, end_y, 6)
        sleep(1)
        draggable_nickname = ''
        dragabbles = self.altdriver.find_elements('DraggableStickerPrefab(Clone)')
        for i in range(len(dragabbles)):
            if name in dragabbles[i].get_component_property('Byjus.K123.StickerBook.DraggableStickerView', 'stickerNickname'):
                #dragabbles[i].mobile_dragTo(end_x, end_y, 3000)
                draggable_nickname = dragabbles[i].get_component_property('Byjus.K123.StickerBook.DraggableStickerView', 'stickerNickname')
                print draggable_nickname
                break
        assert name in draggable_nickname
        self.delete_object_and_verify('DraggableStickerPrefab(Clone)', name)
