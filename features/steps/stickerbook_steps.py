from time import sleep
import sys
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../app/'))
from stickerbook import StickerBook

sys.path.append(PATH('../../generics/'))
import constants
import generics_lib

sys.path.append(PATH('./'))
from generic_steps import GenericStep

class StickerBookSteps(GenericStep):
    
    stickerbook = None
    
    @step('draw on sticker book from start_x: "{start_xvalue}" end_x: "{end_xvalue}" start_y: "{start_yvalue}" end_y: "{end_yvalue}"')
    def stickerbook_draw(self, start_xvalue, end_xvalue, start_yvalue, end_yvalue):
        self.stickerbook = StickerBook(self.obj.altdriver, self.obj.driver)
        self.stickerbook.stickerbook_draw(float(start_xvalue), float(end_xvalue), float(start_yvalue), float(end_yvalue))
        
    @step('perform actions on stickerbook')
    def stickerbook_actions(self):
        self.stickerbook = StickerBook(self.obj.altdriver, self.obj.driver)
    
        for row in self.table:
            generics_lib.takescreenshot(self.obj.driver, PATH('../../compare_images/sticker_1.png'))
            self.base_class.tap('OpenDoodle')
            self.base_class.tap(row['object_name'])
            self.base_class.tap('CloseDoodleArrow/Image')
            sleep(0.5)
            self.stickerbook.stickerbook_draw(float(row['start_x']), float(row['end_x']), float(row['start_y']), float(row['end_y']))
            generics_lib.takescreenshot(self.obj.driver, PATH('../../compare_images/sticker_2.png'))
            assert generics_lib.compare_images(PATH('../../compare_images/sticker_1.png'), PATH('../../compare_images/sticker_2.png')) > 50
        
    @step('drag sticker to the book and verify')
    def drag_sticker(self):
        self.stickerbook = StickerBook(self.obj.altdriver, self.obj.driver)
        for row in self.table:
            self.stickerbook.drag_object_and_verify(row['object_name'], row['nick_name'], float(row['end_x']), float(row['end_y']))
            
    @step('drag sticker to delete and verify')
    def delete_object_and_verify(self):
        self.stickerbook = StickerBook(self.obj.altdriver, self.obj.driver)
        for row in self.table:
            self.stickerbook.delete_object_and_verify(row['object_name'], row['nick_name'])

    @step('drag and drop any sticker from category "{sticker_name}" to scene and delete')
    def drag_delete_sticker_from_category(self, sticker_name):
        self.stickerbook = StickerBook(self.obj.altdriver, self.obj.driver)
        self.stickerbook.drag_delete_stickers_from_category(sticker_name)
    
    @step('drag and drop any sticker from category "{sticker_name}" to scene')
    def drag_sticker_from_category(self, sticker_name):
        self.stickerbook = StickerBook(self.obj.altdriver, self.obj.driver)
        self.stickerbook.drag_stickers_from_category(sticker_name)
            
    @step('draw a line with colour "{colour_name}" and erase')
    def draw_erase(self, colour_name):
        self.stickerbook = StickerBook(self.obj.altdriver, self.obj.driver)
        self.stickerbook.tap('OpenDoodle')
        colour_name = self.obj.altdriver.find_element_where_name_contains(colour_name).name
        self.stickerbook.tap(colour_name)
        self.stickerbook.tap('CloseDoodleArrow')
        generics_lib.takescreenshot(self.obj.driver, PATH('../../compare_images/'+colour_name+'.png'))
        self.stickerbook.stickerbook_draw(float(0.2), float(0.8), float(0.8), float(0.2))
        self.stickerbook.stickerbook_draw(float(0.8), float(0.2), float(0.8), float(0.2))
        generics_lib.takescreenshot(self.obj.driver, PATH('../../compare_images/'+colour_name+'_draw.png'))
        value = generics_lib.pixel_comparision(PATH('../../compare_images/'+colour_name+'.png'), PATH('../../compare_images/'+colour_name+'_draw.png'))
        assert value > 10, 'Images does not match '+ str(value)
        self.stickerbook.tap('OpenDoodle')
        self.stickerbook.tap('EraserSelector')
        self.stickerbook.tap('CloseDoodleArrow')
        self.stickerbook.stickerbook_draw(float(0.2), float(0.8), float(0.8), float(0.2))
        self.stickerbook.stickerbook_draw(float(0.8), float(0.2), float(0.8), float(0.2))
        generics_lib.takescreenshot(self.obj.driver, PATH('../../compare_images/'+colour_name+'_erase.png'))
        value = generics_lib.pixel_comparision(PATH('../../compare_images/'+colour_name+'.png'), PATH('../../compare_images/'+colour_name+'_erase.png'))
        assert  value > 10, 'Images does not match '+ str(value)
        
    @step('draw a line with colour "{colour_name}"')
    def draw(self, colour_name):
        self.stickerbook = StickerBook(self.obj.altdriver, self.obj.driver)
        self.stickerbook.tap('OpenDoodle')
        colour_name = self.obj.altdriver.find_element_where_name_contains(colour_name).name
        self.stickerbook.tap(colour_name)
        self.stickerbook.tap('CloseDoodleArrow')
        generics_lib.takescreenshot(self.obj.driver, PATH('../../compare_images/'+colour_name+'.png'))
        self.stickerbook.stickerbook_draw(float(0.2), float(0.8), float(0.8), float(0.2))
        self.stickerbook.stickerbook_draw(float(0.8), float(0.2), float(0.8), float(0.2))
        generics_lib.takescreenshot(self.obj.driver, PATH('../../compare_images/'+colour_name+'_draw.png'))
        value = generics_lib.color_comparision(PATH('../../compare_images/'+colour_name+'.png'), PATH('../../compare_images/'+colour_name+'_draw.png'))
        assert value > 10, 'Images does not match '+ str(value)
        
    @step('erase the drawn line "{colour_name}"')
    def erase_drawn(self, colour_name):
        self.stickerbook = StickerBook(self.obj.altdriver, self.obj.driver)
        self.stickerbook.tap('OpenDoodle')
        self.stickerbook.tap('EraserSelector')
        colour_name = self.obj.altdriver.find_element_where_name_contains(colour_name).name
        self.stickerbook.tap('CloseDoodleArrow')
        generics_lib.takescreenshot(self.obj.driver, PATH('../../compare_images/'+colour_name+'_draw2.png'))
        value = generics_lib.color_comparision(PATH('../../compare_images/'+colour_name+'_draw2.png'), PATH('../../compare_images/'+colour_name+'_draw.png'))
        assert  value > 10, 'Images does not match '+ str(value)
        self.stickerbook.stickerbook_draw(float(0.2), float(0.8), float(0.8), float(0.2))
        self.stickerbook.stickerbook_draw(float(0.8), float(0.2), float(0.8), float(0.2))
        generics_lib.takescreenshot(self.obj.driver, PATH('../../compare_images/'+colour_name+'_erase.png'))
        value = generics_lib.color_comparision(PATH('../../compare_images/'+colour_name+'_draw2.png'), PATH('../../compare_images/'+colour_name+'_erase.png'))
        assert  value > 10, 'Images does not match '+ str(value)
        