# -*- coding: utf-8 -*-

from altunityrunner.runner import AltrunUnityDriver
from appium import webdriver
from time import sleep
import sys
from ast import literal_eval

from appium.webdriver.connectiontype import ConnectionType
import json
from decimal import Decimal
import subprocess
from numpy.core.defchararray import lower

def launch_app(platform):
    desired_caps = {}
    if 'android' in platform:
        desired_caps['platformName'] = 'android'
        desired_caps['deviceName'] = 'device'
        desired_caps['newCommandTimeout'] = 300
        desired_caps['noReset'] = True
        desired_caps['appPackage'] = "com.byjus.k3"
        desired_caps['appActivity'] = "com.byjus.unity.support.activities.MainActivity"
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        altdriver = AltrunUnityDriver(driver, platform, requestEnd='#')
        altdriver.wait_for_current_scene_to_be('ProfileSelectionScene')
#         altdriver.wait_for_element_to_not_be_present('Interstitial')
        print '==================================================================='
        print driver.orientation
        #altdriver.wait_for_element_to_not_be_present('Interstitial')
#         sleep(30)
        elements = altdriver.find_elements('Profile(Clone)')
        for ele in elements:
            print ele
        
        #driver.find_element_by_image('C:\\Users\\Vinayaka\\Downloads\\country.PNG').click()
        #print altdriver.find_element('Building_1(Clone)').get_component_property('Byjus.K123.GameMapScreen.BuildingView', 'buildingNames')
        '''
        altdriver.wait_for_element('fan_03').mobile_tap()
        altdriver.wait_for_current_scene_to_be('Quests')
        altdriver.wait_for_element_to_not_be_present('Interstitial')
        sleep(8)
        dSize = (driver.get_window_size())
        width = int(dSize['width']) - 20
        x_value = 0
        direction = 'right'
        value = 0
        while x_value > width or x_value < 20:
            elements = altdriver.find_elements_where_name_contains('QuestItem')
            act_text = ''
            for i in range(len(elements)):
                try:
                    act_text = elements[i].get_component_property('Byjus.K123.Quests.QuestListViewItem', 'questNickname')
                except:
                    print 'property not present'
                if 'g3mq61' in act_text:
                    x_value = int(elements[i].x)
                    if value == json.loads(altdriver.wait_for_element('Main Camera').get_component_property("UnityEngine.Transform", "localPosition"))['x']:
                        direction = 'left'
                    if x_value > width or x_value < 20: 
                        if direction == 'left':
                            scroll(driver, 0.3, 0.6, 0.5, 0.5, 1200)
                        elif direction == 'right':
                            scroll(driver, 0.6, 0.3, 0.5, 0.5, 1200)
                        value = json.loads(altdriver.wait_for_element('Main Camera').get_component_property("UnityEngine.Transform", "localPosition"))['x']
                    elif x_value < width or x_value > 20:
                        elements[i].tap()
                    break
        '''        
        '''
        print 'navigate to video'
        #altdriver.wait_for_element('Stickerbook').tap()
        #altdriver.wait_for_current_scene_to_be('stickerbook')
        sleep(100)
        print 'taking'
        directory = 'C:\\Users\\Vinayaka\\Downloads\\test1.png'
        driver.save_screenshot(directory)
        print ' tap wrong answer '
        sleep(10)
        print 'taking'
        directory = 'C:\\Users\\Vinayaka\\Downloads\\test2.png'
        driver.save_screenshot(directory)
        print 'tap correct answer'
        sleep(1)
        print 'taking'
        directory = 'C:\\Users\\Vinayaka\\Downloads\\test3.png'
        driver.save_screenshot(directory)
        '''
        #value = altdriver.wait_for_element('InputFieldPrefab/Text').get_text()
        #print 'd'+value+'b'
        #print type(value)
        '''
        value = altdriver.wait_for_element('LibraryButton').get_component_property("UnityEngine.RectTransform", "localRotation")
        print value
        print type(value)
        t = literal_eval(value)
        print t
        print type(t)
        print t[0]
        print type(t[0])
        '''
        #altdriver.wait_for_element('arrowIndicator').mobile_tap()
        #print altdriver.wait_for_element('Item 1: UAE/Item Label').get_text()
        '''
        value2 = altdriver.wait_for_element('LibraryButton').get_component_property("UnityEngine.RectTransform", "localScale")
        print value2
        print type(value2)
        d = json.loads(value2)
        print d 
        print type(d)
        print d['x']
        print type(d['x'])
        print d['y']
        print type(d['y'])
        print d['z']
        print type(d['z'])
        '''
        '''
        altdriver.wait_for_current_scene_to_be('GameMapScreen')
        sleep(10)
        altdriver.wait_for_element('LibraryButton/Text').mobile_tap(5)
        parental_access('ParentGatePanel/Question', altdriver)
        altdriver.wait_for_current_scene_to_be('Library')
        sleep(10)
        text_tap('Header', 'Batch 1 - V1 (Old)', altdriver)
        sleep(3)
        text_tap('Text', 'Games', altdriver)
        sleep(3)
        text_tap('Header', 'G3MQ30-Match1', altdriver)
        altdriver.wait_for_current_scene_to_be('classification')
        sleep(10)
        altdriver.wait_for_element_where_name_contains('&DraggableObject_1Stage_1')
        '''
        
        
#DraggableObject2degree(Clone)&DraggableObject_1Stage_1        
def parental_access(question, altdriver):
        
        question1 =  get_text(question, altdriver)
        question = question1.split(' ')
        answer = None
        if question[1] == 'x':
            answer = (int(question[0])) * (int(question[2]))
        elif question[1] == '+':
            answer = (int(question[0])) + (int(question[2]))
        elif question[1] == '-':
            answer = (int(question[0])) - (int(question[2]))
        else:
            print 'Math operation unidentified'
            
        print 'Answer for ' + question1 + ' ' + str(answer)
        ans = str(answer)
        keys = altdriver.find_elements('Text')
        
        for j in range(len(ans)):
            for i in range(len(keys)):
                try:
                    if ans[j] == keys[i].get_text():
                        keys[i].tap()
                except:
                    break
        
def get_text(object_name, altdriver):
        text = None
        try:
            text = altdriver.wait_for_element(object_name).get_text()
        except:
            text = altdriver.wait_for_element(object_name).get_component_property("TMPro.TextMeshPro", "text", "Unity.TextMeshPro")
        return text
    
def text_tap(object_name, text, altdriver):
        altdriver.wait_for_element(object_name)
        
        elements = altdriver.find_elements(object_name)
        for element in elements:
            object_text = ''
            try:
                try:
                    object_text = element.get_text()
                except:
                    object_text = element.get_component_property("TMPro.TextMeshPro", "text", "Unity.TextMeshPro")
            except:
                print 'No text property'
            if text in object_text:
                try:
                    element.tap()
                except:
                    element.mobile_tap()
                    
def scroll(driver, start_xvalue, end_xvalue, start_yvalue, end_yvalue, duration):
    dSize = (driver.get_window_size())
    print 'width--------------------'
    print dSize['width']
    print 'height--------------------'
    print dSize['height']
    start_x = (dSize['width']*start_xvalue)
    end_x = (dSize['width']*end_xvalue)
    start_y = (dSize['height']*start_yvalue)
    end_y = (dSize['height']*end_yvalue)
    driver.swipe(start_x, start_y, end_x, end_y, duration)
    
#launch_app('android')
'''
text = "The <color=#7030A0>-ad</color> word family crate has: l<color=#7030A0>ad</color> and gl<color=#7030A0>ad</color>. The <color=#7030A0>-ank</color> word family crate has: pl<color=#7030A0>ank</color>"

text3 = text.replace('<', '+@')

text3 = text3.replace('>', '+')
#print text3
text4 = text3.split('+')
blank = ''
#print text4

for i in range(len(text4)):
    if '@' not in text4[i]:
        blank =  blank + text4[i]
        
print blank
'''

'''
text = 'Tap the letters in the correct order to spell a word that rhymes with â€œtap.â€?'
print '---------'
text2 = text.split()
text = " ".join(text2)
print '---------'
text = str(text)
if 'â€œ' in text:
    text = text.replace('â€œ', '"')
if 'â€' in text:
    text = text.replace('â€', '"')
if 'â€™' in text:
    text = text.replace('â€™', "'")

print text
'''


'''
import subprocess
tee=subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE)
stdout = tee.communicate()[0]
sttt=str('STDOUT:{}'.format(stdout))
nam=sttt.split()
val= len(sttt.split())
for i in range(val):
    if(nam[i]=='device'):
        print(nam[i-1])
'''

