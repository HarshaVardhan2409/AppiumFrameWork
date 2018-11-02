from time import sleep
import sys
import os
from string import lower

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../../../generics/'))
import generics_lib


class BaseClass():
    '''
    This class contains the methods/actions that can be commonly used for all the templates
    '''
    
    altdriver = None
    driver = None

    def __init__(self, altdriver, driver):
        self.altdriver = altdriver
        self.driver = driver
        
    def start_game(self, game_name):
        self.altdriver.wait_for_element_where_name_contains(game_name).tap()
        
    def start_game_with_text(self, text_field, text, load_button):
        self.enter_text(text_field, text)
        self.altdriver.wait_for_element_where_name_contains(load_button).tap()
        
    def start_game_with_text_url(self, text_field, text, url_field, url, load_button):
        self.enter_text(text_field, text)
        self.enter_text(url_field, url)
        self.altdriver.wait_for_element_where_name_contains(load_button).tap()
        
    def wait_for_scene(self, scene_name):
        self.altdriver.wait_for_current_scene_to_be(scene_name)
        
    def verify_scene(self, scene_name):
        assert scene_name in self.altdriver.get_current_scene()
        
    def verify_the_element_on_screen(self, element_name):
            self.altdriver.wait_for_element_where_name_contains(element_name)
            
    def get_object_location(self, object_name):
        x = self.altdriver.wait_for_element_where_name_contains(object_name).x
        y = self.altdriver.wait_for_element_where_name_contains(object_name).y
        value = {"x": x, "y": y}
        return value
    
    def get_object_name(self, object_name):
        value = self.altdriver.wait_for_element_where_name_contains(object_name).name
        return value

    def verify_question(self, object_name, question_number):
        name = self.get_object_name(question_number)
        assert question_number in name
    
    def verify_object_location(self, start_position, end_position, check_status):
        if 'false' in check_status:
            assert int(start_position['x']) == int(end_position['x']) and int(start_position['y']) == int(end_position['y'])
        elif 'true' in check_status:
            assert int(start_position['x']) != int(end_position['x']) or int(start_position['y']) != int(end_position['y'])
            
    def enter_text(self, object_name, text):
        self.altdriver.wait_for_element_where_name_contains(object_name).tap()
        #wait time for keypad to load
        sleep(2)
        generics_lib.action_sendkeys(self.driver, text)
        try:
            self.driver.find_element_by_xpath('//android.widget.Button[@text="OK"]').click()
        except:
            print ''
       
    def  enter_text_app(self, object_name, text):
        self.altdriver.wait_for_element_where_name_contains(object_name).tap()
        #wait time for keypad to load
        sleep(2)
        keycodes = {"0": 7, "1": 8, "2":9, "3":10, "4":11, "5":12, "6":13, "7":14, "8":15, "9":16, "a":29, "b":30, "c":31, "d":32,
             "e":33, "f":34, "g":35, "h":36, "i":37, "j":38, "k":39, "l":40, "m":41, "n":42, "o":43, 
            "p":44, "q":45, "r":46, "s":47, "t":48, "u":49, "v":50, "w":51, "x":52, "y":53, "z":54, "@": 77}
        text = str(text)
        for i in range(len(text)):
            try:
                self.driver.press_keycode(keycodes[text[i]])
            except:
                self.driver.press_keycode(keycodes[lower(text[i])], 1048576)
        try:       
            self.driver.find_element_by_xpath('//android.widget.Button[@text="OK"]').click()
        except:
            print ''
    
    def wait_for_element_display(self, object_name):
        value1 = self.get_object_location(object_name)
        #wait time for element to appear on screen
        sleep(2)
        value2 = self.get_object_location(object_name)
        count = 0
        while int(value1['x']) == int(value2['x']) and int(value1['y']) == int(value2['y']):
            sleep(1)
            value2 = self.get_object_location(object_name)
            count = count + 1
            if count == 10:
                break
            
    def level_successful_message(self, object_name, expected_text):
        actual_text = self.altdriver.wait_for_element_where_name_contains(object_name).get_text()
        assert expected_text in actual_text
        
    def verify_text(self, object_name, expected_text):
        actual_text = self.altdriver.wait_for_element_where_name_contains(object_name).text
        assert expected_text in actual_text
        
    def tap(self, object_name):
        self.altdriver.wait_for_element(object_name).tap()
        
    def tap_and_hold(self, object_name, duration):
        self.altdriver.wait_for_element(object_name).mobile_tap(duration)
            