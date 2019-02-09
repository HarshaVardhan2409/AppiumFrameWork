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
            generics_lib.takescreenshot(self.obj.driver, PATH('../../compare_images/image_1.png'))
            self.base_class.tap('OpenDoodle')
            self.base_class.tap(row['object_name'])
            self.base_class.tap('CloseDoodleArrow/Image')
            sleep(1)
            self.stickerbook.stickerbook_draw(float(row['start_x']), float(row['end_x']), float(row['start_y']), float(row['end_y']))
            generics_lib.takescreenshot(self.obj.driver, PATH('../../compare_images/image_2.png'))
            assert generics_lib.compare_images(PATH('../../compare_images/image_1.png'), PATH('../../compare_images/image_2.png')) > 50
        
        
        