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
        
        