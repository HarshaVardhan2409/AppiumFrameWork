from time import sleep
import sys
import os
from string import lower
from selenium.webdriver.common.by import By
from altunityrunner import AltrunUnityDriver
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../../../generics/'))
import generics_lib
import constants


class BaseClass():
    '''
    This class contains the methods/actions that can be commonly used for all the templates
    '''
    
    altdriver = None
    driver = None
    platform = None
    desired_caps = None
    
    def __init__(self, altdriver, driver):
        self.altdriver = altdriver
        self.driver = driver
    
    def start_game(self, game_name):
        self.tap(game_name)
        
    def start_game_with_text(self, text_field, text, load_button):
        self.enter_text(text_field, text)
        self.tap(load_button)
        
    def start_game_with_text_url(self, text_field, text, url_field, url, load_button):
        self.enter_text(text_field, text)
        self.enter_text(url_field, url)
        self.tap(load_button)
            
    def wait_for_scene(self, scene_name):
        self.altdriver.wait_for_current_scene_to_be(scene_name)
        
    def verify_scene(self, scene_name):
        assert scene_name in self.altdriver.get_current_scene()
        
    def verify_the_element_on_screen(self, element_name):
            self.altdriver.wait_for_element(element_name)
            
    def get_object_location(self, object_name):
        x = self.altdriver.wait_for_element(object_name).x
        y = self.altdriver.wait_for_element(object_name).y
        value = {"x": x, "y": y}
        return value
    
    def get_object_name(self, object_name):
        value = self.altdriver.wait_for_element_where_name_contains(object_name).name
        return value

    def verify_question(self, object_name):
        name = self.altdriver.wait_for_element(object_name).name
        assert object_name in name
    
    def verify_object_location(self, start_position, end_position, check_status):
        if 'false' in check_status:
            assert int(start_position['x']) == int(end_position['x']) and int(start_position['y']) == int(end_position['y'])
        elif 'true' in check_status:
            assert int(start_position['x']) != int(end_position['x']) or int(start_position['y']) != int(end_position['y'])
    
    def wait_for_element_display(self, object_name):
        value1 = self.get_object_location(object_name)
        #wait time for element to appear on screen
        sleep(2)
        value2 = self.get_object_location(object_name)
        count = 0
        while int(value1['x']) == int(value2['x']) and int(value1['y']) == int(value2['y']):
            sleep(0.3)
            value2 = self.get_object_location(object_name)
            count = count + 1
            if count == 20:
                break
        
    def verify_text(self, object_name, expected_text):
        actual_text = self.get_text(object_name)
        value = self.check_status(object_name)
        count = 0
        while 'rue' not in value:
            sleep(0.2)
            count += 1
            if count >=20:
                break
        assert 'rue' in value
        assert expected_text in actual_text
        
    def verify_text_for_duplicate_objects(self, object_name, expected_text):
        elements = self.altdriver.find_elements(object_name)
        for i in range(len(elements)):
            try:
                actual_text = elements[i].get_text()
            except:
                actual_text = elements[i].get_component_property("TMPro.TextMeshPro", "text", "Unity.TextMeshPro")
            if expected_text in actual_text:
                break
        assert expected_text in actual_text
        
    def enter_text(self, object_name, text):
        self.tap(object_name)
        #wait time for keypad to load
        sleep(2)
        generics_lib.action_sendkeys(self.driver, text)
        try:
            self.driver.find_element_by_xpath('//android.widget.Button[@text="OK"]').click()
        except:
            print 'No ok button'
       
    def  enter_text_app(self, object_name, text):
        self.altdriver.wait_for_element(object_name)
        #wait time for keypad to load
        sleep(2)
        self.tap(object_name)
        #wait time for keypad to load
        sleep(1)
        keycodes = {"0": 7, "1": 8, "2":9, "3":10, "4":11, "5":12, "6":13, "7":14, "8":15, "9":16, "a":29, "b":30, "c":31, "d":32,
             "e":33, "f":34, "g":35, "h":36, "i":37, "j":38, "k":39, "l":40, "m":41, "n":42, "o":43, 
            "p":44, "q":45, "r":46, "s":47, "t":48, "u":49, "v":50, "w":51, "x":52, "y":53, "z":54, "@": 77, '"': 75, "\\": 73, ",": 55, "=": 70, "[": 71, "]": 72, "-": 69, ";": 74, "/": 76, " ":62}
        text = str(text)
        for i in range(len(text)):
            try:
                self.driver.press_keycode(keycodes[text[i]])
            except:
                self.driver.press_keycode(keycodes[lower(text[i])], 1048576)
    
    def get_text(self, object_name):
        text = None
        try:
            text = self.altdriver.wait_for_element(object_name).get_text()
        except:
            text = self.altdriver.wait_for_element(object_name).get_component_property("TMPro.TextMeshPro", "text", "Unity.TextMeshPro")
        return text
        
    def tap(self, object_name):
        self.altdriver.wait_for_element(object_name)
        sleep(0.5)
        try:
            self.altdriver.wait_for_element(object_name).mobile_tap()
        except:
            self.altdriver.wait_for_element(object_name).mobile_tap()
            
    def text_tap(self,object_name, text):
        self.altdriver.wait_for_element(object_name)
        
        elements = self.altdriver.find_elements(object_name)
        for element in elements:
            object_text = ''
            try:
                try:
                    object_text = element.get_text()
                except:
                    object_text = element.get_component_property("TMPro.TextMeshPro", "text", "Unity.TextMeshPro")
            except:
                print 'No text property'
            try:
                if text in object_text:
                    try:
                        element.tap()
                    except:
                        element.mobile_tap()
            except:
                print "'ascii' codec can't decode"
                    
    def tap_element_text(self, text):
        if '@' == text:
            self.driver.find_element(By.XPATH, "//*[contains(@text,'"+text+"')]").click()
        else:
            self.driver.find_element(By.XPATH, "//*[@text='"+text+"']").click()
        
    def scroll_verify(self, object_name, start_xvalue, end_xvalue, start_yvalue, end_yvalue):
        start_position = self.get_object_location(object_name)
        generics_lib.scroll(self.driver, start_xvalue, end_xvalue, start_yvalue, end_yvalue)
        end_position = self.get_object_location(object_name)
        self.verify_object_location(start_position, end_position, 'true')
        
    def tap_and_hold(self, object_name, duration):
        self.altdriver.wait_for_element(object_name).mobile_tap(int(duration))
        
    def verify_native_text(self, text):
        assert  self.driver.find_element(By.XPATH, "//*[@text='"+text+"']").is_displayed()
        
    def clear_text(self, object_name):
        #self.tap(object_name)
        sleep(1.5)
        value = self.get_text(object_name)
        count = 0
        while value != '' and count <= 20 :
            self.altdriver.wait_for_element(object_name).mobile_tap()
            self.altdriver.wait_for_element(object_name).mobile_tap(0.1)
            self.altdriver.wait_for_element(object_name).mobile_tap(0.1)
            sleep(0.4)
            self.driver.press_keycode(67)
            sleep(0.4)
            value = self.get_text(object_name)
            count += 1
        value = self.get_text(object_name)
        assert '' == value
            
    def click_back(self):
        sleep(1)
        self.driver.press_keycode(4)
        
    def home_button(self):
        sleep(1)
        self.driver.press_keycode(3)   
            
    def check_status(self, object_name):
        print '-----------------------------------------------------------------'
        value1 = None
        value2 = None
        try:
            value1 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.UI.Text", "enabled")
        except:
            value1 = self.altdriver.wait_for_element(object_name).get_component_property("TMPro.TextMeshPro", "enabled", "Unity.TextMeshPro")
        '''    
        try:
            value2 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.UI.Text", "isActiveAndEnabled")
        except:
            print 'isActive is fail'
        '''
        return value1
            