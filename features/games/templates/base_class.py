# -*- coding: utf-8 -*-

from ast import literal_eval
import os
from string import lower
import sys
from time import sleep

from altunityrunner import AltrunUnityDriver
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from _socket import timeout

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../../../generics/'))
import constants
import generics_lib
import json

class BaseClass():
    '''
    This class contains the methods/actions that can be commonly used for all the templates
    '''
    
    altdriver = None
    driver = None
    platform = None
    desired_caps = None
    i=1
    flag=False
    checkmark_list=[]
    index=0
    ele_y=[]
    
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

    def tap_image(self, image_name):
        self.driver.find_element_by_image(PATH('../../../a_image/'+image_name)).click()

    def verify_image(self, image_name):
        self.driver.find_element_by_image(PATH('../../../a_image/'+image_name)).is_displayed()

    def wait_for_scene(self, scene_name):
        self.altdriver.wait_for_current_scene_to_be(scene_name)
        
    def wait_for_element_not_present(self, object_name):
        self.altdriver.wait_for_element_to_not_be_present(object_name, timeout=40)
        
    def verify_scene(self, scene_name):
        print 'entered verified'
        self.wait_for_scene(str(scene_name))
        print 'wait completed'
        assert str(scene_name) in self.altdriver.get_current_scene()
        
    def verify_the_element_on_screen(self, element_name):
            self.altdriver.wait_for_element(element_name, timeout=60)
            sleep(2)
            
    def get_object_location(self, object_name):
        x = self.altdriver.wait_for_element(object_name).x
        y = self.altdriver.wait_for_element(object_name).y
        value = {"x": x, "y": y}
        return value
    
    def get_object_name(self, object_name):
        value = self.altdriver.wait_for_element_where_name_contains(object_name).name
        return value

    def verify_question(self, object_name):
        name = self.altdriver.wait_for_element(object_name, timeout=60).name
        assert object_name in name
    
    def verify_object_location(self, start_position, end_position, check_status):
        if 'false' in lower(check_status):
            assert int(start_position['x']) == int(end_position['x']) and int(start_position['y']) == int(end_position['y'])
        elif 'true' in lower(check_status):
            assert int(start_position['x']) != int(end_position['x']) or int(start_position['y']) != int(end_position['y'])
    
    def wait_for_element_display(self, object_name, exit_count=20):
        value1 = self.get_object_location(object_name)
        rotation1 = None
        rotation2 = None
        try:
            print 'entering try'
            rotation1 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.RectTransform", "localRotation")
            rotation1 = literal_eval(rotation1)
            scale1 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.RectTransform", "localScale")
            scale1 = json.loads(scale1)
            #wait time for element to appear on screen
            sleep(2)
            rotation2 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.RectTransform", "localRotation")
            rotation2 = literal_eval(rotation2)
            scale2 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.RectTransform", "localScale")
            scale2 = json.loads(scale2)
        except:
            print 'entering except'
            rotation1 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.Transform", "localRotation")
            rotation1 = literal_eval(rotation1)
            scale1 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.Transform", "localScale")
            scale1 = json.loads(scale1)
            #wait time for element to appear on screen
            sleep(2)
            rotation2 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.Transform", "localRotation")
            rotation2 = literal_eval(rotation2)
            scale2 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.Transform", "localScale")
            scale2 = json.loads(scale2)
        value2 = self.get_object_location(object_name)
        if 'dict' in str(type(rotation2)):
            rotation1 = (rotation1['x'], rotation1['y'], rotation1['z'])
            rotation2 = (rotation2['x'], rotation2['y'], rotation2['z'])
        count = 0
        while ((int(value1['x']) == int(value2['x']) and int(value1['y']) == int(value2['y'])) and 
               ((rotation1[0] == rotation2[0]) and (rotation1[1] == rotation2[1]) and (rotation1[2] == rotation2[2])) and
               ((scale1['x'] == scale2['x']) and (scale1['y'] == scale2['y']))):
            sleep(0.3)
            value2 = self.get_object_location(object_name)
            try:
                rotation2 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.RectTransform", "localRotation")
                rotation2 = literal_eval(rotation2)
                scale2 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.RectTransform", "localScale")
                scale2 = json.loads(scale2)
            except:
                rotation2 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.Transform", "localRotation")
                rotation2 = literal_eval(rotation2)
                scale2 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.Transform", "localScale")
                scale2 = json.loads(scale2)
            if 'dict' in str(type(rotation2)):
                rotation2 = (rotation2['x'], rotation2['y'], rotation2['z'])
            count = count + 1
            if count == exit_count:
                break
    
    def wait_for_element_contains_text(self, object_name, text):
        self.altdriver.wait_for_element_with_text(object_name, text)
        
    def verify_text(self, object_name, expected_text):
        try:
            self.altdriver.wait_for_element(object_name)
            actual_text = self.get_text(object_name)
            actual_text = str(actual_text)
            print '---------'
            text = actual_text.split()
            str4=""
            for i in range(len(text)):
                if text[i].startswith('<'):
                    str3=text[i].split('>')
                    text[i]=str3[1]
                    str4=str4+' '+text[i]
                    print text[i]
                else:
                    str4=str4+' '+text[i]
            actual_text=str4
            print '---------'
            value = self.check_status(object_name)
            count = 0
            while 'rue' not in value:
                sleep(0.2)
                count += 1
                if count >=20:
                    break
            assert 'rue' in value
            print '-----------------------------'
            print actual_text
            print type(actual_text)
            if '”' in actual_text:
                actual_text = actual_text.replace('”', '"')
            if '“' in actual_text:
                actual_text = actual_text.replace('“', '"')
            if '’' in actual_text:
                actual_text = actual_text.replace('’', "'")
            print '----------------================='
            print expected_text
            exp_t="".join(expected_text.split(" "))
            act_t="".join(actual_text.split(" "))
            assert exp_t in act_t
        except:
            self.get_server_logs()
        
        
        
    def verify_text_for_duplicate_objects(self, object_name, expected_text):
        elements = self.altdriver.find_elements(object_name)
        for i in range(len(elements)):
            try:
                actual_text = elements[i].get_text()
            except:
                try:
                    actual_text = elements[i].get_component_property("TMPro.TextMeshPro", "text", "Unity.TextMeshPro")
                except:
                    actual_text = elements[i].get_component_property("TMPro.TextMeshProUGUI", "text", "Unity.TextMeshPro")
            if expected_text in actual_text:
                break
        assert expected_text in actual_text
        
        
    def verify_text_of_component(self, component_name, component_property, object_name, expected_text):
        elements = self.altdriver.find_elements(object_name)
        for i in range(len(elements)):
            try:
                actual_text = elements[i].get_text()
            except:
                actual_text = elements[i].get_component_property(component_name, component_property)
            if expected_text in actual_text:
                break
        assert expected_text in actual_text
        
    def get_component_property(self, object_name, component_name, component_property):
        text = self.altdriver.wait_for_element(object_name).get_component_property(component_name, component_property)  
        return text
        
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
            try:
                text = self.altdriver.wait_for_element(object_name).get_component_property("TMPro.TextMeshPro", "text", "Unity.TextMeshPro")
            except:
                text = self.altdriver.wait_for_element(object_name).get_component_property("TMPro.TextMeshProUGUI", "text", "Unity.TextMeshPro")
        if text != None:
            if '</' in text:
                text1 = text.replace('<', '+@')
                text1 = text1.replace('>', '+')
                text2 = text1.split('+')
                text = ''
                #print text4
                
                for i in range(len(text2)):
                    if '@' not in text2[i]:
                        text =  text + text2[i]
        return text
        
    def tap(self, object_name):
        self.altdriver.wait_for_element(object_name)
        sleep(0.5)
        try:
            self.altdriver.wait_for_element(object_name).tap()
        except:
            self.altdriver.find_element(object_name).mobile_tap()

    def mobiletap(self, object_name):
        self.altdriver.wait_for_element(object_name)
        sleep(0.5)
        self.altdriver.find_element(object_name).mobile_tap()
            
    def text_tap(self,object_name, text):
        self.altdriver.wait_for_element(object_name)
        elements = self.altdriver.find_elements(object_name)
        for element in elements:
            object_text = ''
            try:
                try:
                    object_text = element.get_text()
                except:
                    try:
                        object_text = element.get_component_property("TMPro.TextMeshPro", "text", "Unity.TextMeshPro")
                    except:
                        object_text = element.get_component_property("TMPro.TextMeshProUGUI", "text", "Unity.TextMeshPro")
            except:
                print 'No text property'
            try:
                if text in object_text:
                    try:
                        element.tap()
                        break
                    except:
                        element.mobile_tap()
                        break
            except:
                print "ascii' codec can't decode"
                
                
    def tap_title(self, object_name, title):
        self.altdriver.wait_for_element(object_name)       
        elements = self.altdriver.find_elements(object_name)
        for element in elements:
            object_title = ''
            try:
                object_title = element.get_component_property("Byjus.K123.Tasks.TaskCardView", "title")
            except:
                print 'No title property'
            try:
                if title in object_title:
                    try:
                        element.tap()
                    except:
                        element.mobile_tap()
            except:
                print " "
                    
    def tap_element_text(self, text):
        if '@' == text:
            self.driver.find_element(By.XPATH, "//*[contains(@text,'"+text+"')]").click()
        else:
            self.driver.find_element(By.XPATH, "//*[@text='"+text+"']").click()
        
    def scroll_verify(self, object_name, start_xvalue, end_xvalue, start_yvalue, end_yvalue):
        start_position = self.get_object_location(object_name)
        generics_lib.scroll(self.driver, start_xvalue, end_xvalue, start_yvalue, end_yvalue, 800)
        sleep(0.5)
        end_position = self.get_object_location(object_name)
        self.verify_object_location(start_position, end_position, 'true')
    
    def scroll_verify_for_false(self, object_name, start_xvalue, end_xvalue, start_yvalue, end_yvalue):
        start_position = self.get_object_location(object_name)
        generics_lib.scroll(self.driver, start_xvalue, end_xvalue, start_yvalue, end_yvalue, 600)
        sleep(0.5)
        end_position = self.get_object_location(object_name)
        self.verify_object_location(start_position, end_position, 'false')
    
    def scroll(self, start_xvalue, end_xvalue, start_yvalue, end_yvalue):
        generics_lib.scroll(self.driver, start_xvalue, end_xvalue, start_yvalue, end_yvalue, 600)
        
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
#             self.altdriver.wait_for_element(object_name).mobile_tap()
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
        
    def put_app_background(self):
        sleep(1)    
        self.driver.background_app(5)

    def check_status(self, object_name):
        print '-----------------------------------------------------------------'
        value1 = None
        value2 = None
        try:
            value1 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.UI.Text", "enabled")
        except:
            try:
                value1 = self.altdriver.wait_for_element(object_name).get_component_property("TMPro.TextMeshPro", "enabled", "Unity.TextMeshPro")
            except:
                value1 = self.altdriver.wait_for_element(object_name).get_component_property("TMPro.TextMeshProUGUI", "enabled", "Unity.TextMeshPro")
        '''    
        try:
            value2 = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.UI.Text", "isActiveAndEnabled")
        except:
            print 'isActive is fail'
        '''
        return value1
            
    def verify_orientation(self, expected_orientation):
        actual_orientation = self.driver.orientation
        assert lower(expected_orientation) in lower(actual_orientation)
        
    def select_game(self, expected_text, object_name):
        i = 0
        sleep(2)
        while i < 12:
            i += 1
            try:
                print object_name
                print expected_text
                self.verify_text_for_game_objects(object_name, expected_text)
                break
            except:
                self.scroll_verify('Content', 0.5, 0.5, 0.8, 0.3)
                sleep(1)
                
    def verify_text_for_game_objects(self, object_name, expected_text):
            elements = self.altdriver.find_elements(object_name)
            for i in range(len(elements)):
                actual_text = elements[i].get_text()
                #actual_text = actual_text.split(' ')
                expected_text = str(expected_text)
                #actual_text = actual_text[0]
                if expected_text in actual_text:
                    print 'found........................................................................'
                    sleep(0.5)
                    elements[i].tap()
                    break
            assert expected_text in actual_text
       
    """def verify_text_for_game_objects(self, object_name, expected_text):
        elements = self.altdriver.find_elements(object_name)
        for i in range(len(elements)):
            actual_text = elements[i].get_text()
            actual_text = actual_text.split(' ')
            expected_text = str(expected_text)
            actual_text = actual_text[0]
            if expected_text in actual_text:
                print 'found........................................................................'
                sleep(0.5)
                elements[i].tap()
                break
        assert expected_text in actual_text"""

    """def verify_presence_of_hint(self,object_name):
    # try:
        self.altdriver.wait_for_element(object_name)
        #except:
        try:
            glow_range = float(self.altdriver.wait_for_element(object_name).get_component_property("Byjus.K123.Common.SpriteGlow", "alphaRange"))
            
            #glow_range = self.altdriver.wait_for_element(object_name).get_component_property("Byjus.K123.Templates.MCQ.SpriteOuterGlow", "alphaRange")
            print glow_range
            #self.assertNotEqual(glow_range, 0)
        except:
            print "hint not displayed"
        assert glow_range > 0"""
        
    def verify_presence_of_hint(self,object_name):
        try:
            try:
                self.altdriver.wait_for_element(object_name)
            except:
                try:
                    self.altdriver.wait_for_element(object_name).get_component_property("Byjus.K123.Templates.MCQ.SpriteOuterGlow", "glowColor")
                except:
                    print "hint not dispayed"
                    #assert False
        except:
            self.get_server_logs()
            assert False
            
    def verify_presence_of_hint2(self,object_name):
        self.altdriver.wait_for_element(object_name)
        self.altdriver.wait_for_element(object_name).get_component_property("Byjus.K123.Templates.MCQ.SpriteOuterGlow", "glowColor")
        
    def get_server_logs(self):
        print "=========================creating file==================="
        
        logs=str(self.driver.get_log('server'))
        #print logs
        
        file = open(PATH('../../../execution_data/reports/server_logs/')+sys.argv[6]+str(self.i)+'.txt','w') 
        file.write(logs) 
        file.close() 
        print "=========================created file==================="
        self.i=self.i+1
        print 'success'    
        
        
    def multiple_tap(self,obj1,obj2,obj3,obj4):
        x_point=self.altdriver.find_element(obj4).x
        y_point=self.altdriver.find_element(obj4).mobileY
        TouchAction(self.driver).long_press(None,int(self.altdriver.find_element(obj3).x),int(self.altdriver.find_element(obj3).mobileY),4000)
        sleep(2)
                     
        a1=TouchAction(self.driver)
        a1.tap(None,int(self.altdriver.find_element(obj3).x),int(self.altdriver.find_element(obj3).mobileY))
        a2=TouchAction(self.driver)
        a2.tap(None,int(self.altdriver.find_element(obj2).x),int(self.altdriver.find_element(obj2).mobileY))
        a3=TouchAction(self.driver)
        a3.tap(None,int(self.altdriver.find_element(obj1).x),int(self.altdriver.find_element(obj1).mobileY))
        a4=TouchAction(self.driver)
        a4.tap(None,int(x_point),int(y_point))
        ma = MultiAction(self.driver)
        ma.add(a1,a2,a3,a4)
        ma.perform()
     
    def multiple_drag_and_drop(self,drag1,buckt): 
        sleep(2)
        a1 = TouchAction(self.driver)
        a1.long_press(None,int(self.altdriver.find_element(drag1).x),int(self.altdriver.find_element(drag1).mobileY),500).move_to(None,int(self.altdriver.find_element(buckt).x),int(self.altdriver.find_element(buckt).mobileY))
        a1.release().perform()
        
    def select_batch(self, object_name,expected_text):
        try:
            i = 0
            sleep(2)
            while i < 12:
                i += 1
                try:
                    print object_name
                    print expected_text
                    self.text_tap(object_name, expected_text)
                    break
                except:
                    print "not clicked on element" 
        except:
            self.get_server_logs()
            assert False  

    def verify_favorites(self,video_no):
        sleep(5)
        elements = self.altdriver.find_elements('Header')
        print len(elements)
        for i in range(len(elements)-1):
            if elements[i].get_text() in video_no:
                self.flag=True
                
        print self.flag
        
        if self.flag==True:
            print "successfully added video to favorites"
            self.flag =False
        else:
            assert False, "video is not added"
        
    def adding_video_to_favourite(self,video_no):
        self.click_on_favorite(video_no)
        
    def click_on_favorite(self,video_no):
        print "entered fqvorite method"
        sleep(5)
        while(self.flag==False):
            elements=self.altdriver.find_elements('Header')
            print "value of elements ooo"
            print len(elements)
            
                        
            for i in range(len(elements)-1):
                try:
                    if elements[i].get_text() in video_no:
                        self.index=i
                        e=self.altdriver.find_elements_where_name_contains('Header')
                        for j in range(len(e)-1):
                            if e[j].name == "Checkmark":
                                print "checkmark present"
                                self.checkmark_list.append(e[j])
                                self.flag=True
                        break
                    """else:
                         generics_lib.scroll(self.driver, 0.5, 0.5, 0.3, 0.1, 800)"""
                except:
                    print "ascii error"   
            generics_lib.scroll(self.driver, 0.5, 0.5, 0.3, 0.1, 800)
        print "printing y values................."
        self.checkmark_list[self.index].tap()
        self.flag=False 
        self.checkmark_list=[]
        
        
    def switch_profiles(self,profile_name): 
        profiles=self.altdriver.find_elements('ChildProfileButton(Clone)/name')
        for p in range(len(profiles)):
            if profiles[p].get_text() in profile_name:
                profiles[p].tap()
                
    def select_profiles(self,profile_name):           
        profiles=self.altdriver.find_elements('Name Panel/Text')
        for p in range(len(profiles)):
            if profiles[p].get_text() in profile_name:
                profiles[p].tap()
     
    def switch_grade(self,grade_name):
        current_grade=self.altdriver.find_elements('ChildProfileButton(Clone)/grade')
        current_grade[0].tap()
        print current_grade[0].get_text()
        sleep(5)
        if current_grade[0].get_text() in grade_name:
            sleep(5)            
            self.altdriver.find_element('BackButton').tap()         
            sleep(5)
        else:
            print "entering if.........."
            grade=self.altdriver.find_elements('GradeToggle(Clone)/Image/Text')
            for p in range(len(grade)):
                print "==================="
                if grade[p].get_text().split(' ')[0] in grade_name:
                    sleep(3)
                    a1=TouchAction(self.driver)
                    a1.tap(None,int(self.altdriver.find_elements('GradeToggle(Clone)')[p].x),int(self.altdriver.find_elements('GradeToggle(Clone)')[p].mobileY)).perform()
                    #self.altdriver.find_elements('GradeToggle(Clone)')[p].tap() 
                    self.altdriver.wait_for_element("NotificationToastBar(Clone)")
                    break           
            
            self.altdriver.find_element('BackButton').tap()         