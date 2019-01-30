from altunityrunner.runner import AltrunUnityDriver
from appium import webdriver
from time import sleep
import sys
from ast import literal_eval

from appium.webdriver.connectiontype import ConnectionType
import json

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
        altdriver = AltrunUnityDriver(driver, platform)
        altdriver.wait_for_current_scene_to_be('GameMapScreen')
        sleep(20)
        print '==================================================================='
        print driver.orientation
        #value = altdriver.wait_for_element('InputFieldPrefab/Text').get_text()
        #print 'd'+value+'b'
        #print type(value)
        value = altdriver.wait_for_element('LibraryButton').get_component_property("UnityEngine.RectTransform", "localRotation")
        print value
        print type(value)
        t = literal_eval(value)
        print t
        print type(t)
        print t[0]
        print type(t[0])
        #altdriver.wait_for_element('arrowIndicator').mobile_tap()
        #print altdriver.wait_for_element('Item 1: UAE/Item Label').get_text()
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