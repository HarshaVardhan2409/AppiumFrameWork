import os
import sys
import json
from time import sleep
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../games/templates/'))
from base_class import BaseClass

sys.path.append(PATH('../../generics'))
import generics_lib

class Quests(BaseClass):
    
    
    def verify_quest_progression(self, object_name, text, total_tasks, completed_tasks):
        self.altdriver.wait_for_element_where_name_contains(object_name)
        elements = self.altdriver.find_elements_where_name_contains(object_name)
        act_text = ''
        for i in range(len(elements)):
            try:
                act_text = elements[i].get_component_property('Byjus.K123.Quests.QuestListViewItem', 'questNickname')
            except:
                print 'property not present'
            if text in act_text:
                act_total_tasks = elements[i].get_component_property('Byjus.K123.Quests.QuestListViewItem', 'totalTasks')
                print total_tasks
                print act_total_tasks
                assert total_tasks == act_total_tasks
                act_completed_tasks = elements[i].get_component_property('Byjus.K123.Quests.QuestListViewItem', 'completedTasks')
                print completed_tasks
                print act_completed_tasks
                assert completed_tasks == act_completed_tasks
                break

    def select_task(self, object_name, quest_nickname):
        dSize = (self.driver.get_window_size())
        width = int(dSize['width']) - 20
        x_value = 0
        direction = 'right'
        value = 0
        while x_value > width or x_value < 20:
            elements = self.altdriver.find_elements_where_name_contains(object_name)
            act_text = ''
            for i in range(len(elements)):
                try:
                    act_text = elements[i].get_component_property('Byjus.K123.Quests.QuestListViewItem', 'questNickname')
                except:
                    print 'property not present'
                if quest_nickname in act_text:
                    x_value = int(elements[i].x)
                    if value == json.loads(self.altdriver.wait_for_element('Main Camera').get_component_property("UnityEngine.Transform", "localPosition"))['x']:
                        direction = 'left'
                    if x_value > width or x_value < 20: 
                        if direction == 'left':
                            generics_lib.scroll(self.driver, 0.3, 0.6, 0.5, 0.5, 1200)
                        elif direction == 'right':
                            generics_lib.scroll(self.driver, 0.6, 0.3, 0.5, 0.5, 1200)
                        value = json.loads(self.altdriver.wait_for_element('Main Camera').get_component_property("UnityEngine.Transform", "localPosition"))['x']
                    elif x_value < width or x_value > 20:
                        elements[i].tap()
                    break
                '''
                else:
                    if value == json.loads(self.altdriver.wait_for_element('Main Camera').get_component_property("UnityEngine.Transform", "localPosition"))['x']:
                        if direction == 'left':
                                generics_lib.scroll(self.driver, 0.3, 0.6, 0.5, 0.5, 1200)
                        elif direction == 'right':
                            generics_lib.scroll(self.driver, 0.6, 0.3, 0.5, 0.5, 1200)
                        value = json.loads(self.altdriver.wait_for_element('Main Camera').get_component_property("UnityEngine.Transform", "localPosition"))['x']
                '''
    def select_quest(self, object_name, quest_name):
        
        dSize = (self.driver.get_window_size())
        width = int(dSize['width']) - 50
        x_value = 0
        direction = 'right'
        value = 0
        print object_name
        while x_value > width or x_value < 20:
            elements = self.altdriver.find_elements_by_component('Byjus.K123.GameMapScreen.BuildingView')
            act_text = ''
            for i in range(len(elements)):
                try:
                    act_text = elements[i].get_component_property('Byjus.K123.GameMapScreen.BuildingView', 'buildingNames')
                except:
                    print 'property not present'
                if quest_name in act_text:
                    x_value = int(elements[i].x)
                    print elements[i].toJSON()
                    print x_value
                    if value == json.loads(self.altdriver.wait_for_element('Main Camera').get_component_property("UnityEngine.Transform", "localPosition"))['x']:
                        direction = 'left'
                    if x_value > width or x_value < 50: 
                        if direction == 'left':
                            generics_lib.scroll(self.driver, 0.2, 0.7, 0.5, 0.5, 400)
                        elif direction == 'right':
                            generics_lib.scroll(self.driver, 0.7, 0.2, 0.5, 0.5, 400)
                        value = json.loads(self.altdriver.wait_for_element('Main Camera').get_component_property("UnityEngine.Transform", "localPosition"))['x']
                    elif x_value < width or x_value > 20:
                        elements[i].mobile_tap()
                    break

    def check_avatar_selected(self, object_name, exp_status):
        elements = self.altdriver.find_elements(object_name)
        act_status = None
        flag = False
        for i in range(len(elements)):
            act_status = elements[i].get_component_property('UnityEngine.UI.Image', 'enabled')
            if 'rue' in exp_status:
                if 'rue' in act_status:
                    flag = True
                    break
            elif 'alse' in exp_status:
                if 'alse' in act_status:
                    flag = True
                    break
        assert  flag is True
        
    def check_avatar_highlighted(self, object_name, nickname):
        elements = self.altdriver.find_elements(object_name)
        name = None
        color_selected = None
        others = None
        for i in range(len(elements)):
            name = elements[i].get_component_property('Byjus.K123.ProfileSelection.AvatarView', 'nickname')
            if nickname in name:
                color_selected = elements[i].get_component_property('UnityEngine.UI.RawImage', 'color')
        for i in range(len(elements)):
            name = elements[i].get_component_property('Byjus.K123.ProfileSelection.AvatarView', 'nickname')
            if nickname not in name:
                others = elements[i].get_component_property('UnityEngine.UI.RawImage', 'color')
                assert color_selected != others
        
            
    def select_avatar(self, object_name, avatar_nickname):
        dSize = (self.driver.get_window_size())
        width = int(dSize['width']) - 20
        x_value = 0
        direction = 'right'
        value = 0
        while x_value > width or x_value < 20:
            elements = self.altdriver.find_elements(object_name)
            act_text = ''
            for i in range(len(elements)):
                try:
                    act_text = elements[i].get_component_property('Byjus.K123.ProfileSelection.AvatarView', 'nickname')
                except:
                    print 'property not present'
                if avatar_nickname in act_text:
                    x_value = int(elements[i].x)
                    if value == json.loads(self.altdriver.wait_for_element('AvatarBoothPanel').get_component_property("UnityEngine.RectTransform", "localPosition"))['x']:
                        direction = 'left'
                    if x_value > width or x_value < 20: 
                        if direction == 'left':
                            generics_lib.scroll(self.driver, 0.3, 0.6, 0.5, 0.5, 1200)
                        elif direction == 'right':
                            generics_lib.scroll(self.driver, 0.6, 0.3, 0.5, 0.5, 1200)
                        value = json.loads(self.altdriver.wait_for_element('AvatarBoothPanel').get_component_property("UnityEngine.RectTransform", "localPosition"))['x']
                    elif x_value < width or x_value > 20:
                        elements[i].tap()
                    break
