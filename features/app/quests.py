import os
import sys
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
        for i in range(len(elements)):
            try:
                act_text = elements[i].get_component_property('Byjus.K123.Quests.QuestListViewItem', 'questNickname')
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
            except:
                print 'property not present'

