from time import sleep
import sys
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../app/'))
from quests import Quests

sys.path.append(PATH('../../generics/'))
import constants
import generics_lib

sys.path.append(PATH('./'))
from generic_steps import GenericStep

class QuestsSteps(GenericStep):
    
    quests = None
    
    @step('verify the quest progression')
    def quests_progression(self):
        self.quests = Quests(self.obj.altdriver, self.obj.driver)
        for row in self.table:
            self.quests.verify_quest_progression(row['object_name'], row['text'], row['total_tasks'], row['completed_tasks'])
    
    @step('select the task with element: "{object_name}" and quest nickname: "{quest_nickname}"')
    def select_tasks(self, object_name, quest_nickname):
        self.quests = Quests(self.obj.altdriver, self.obj.driver)
        self.quests.select_task(object_name, quest_nickname)


    @step('select the quest with element: "{object_name}" and quest name: "{quest_name}"')
    def select_quests(self, object_name, quest_name):
        self.quests = Quests(self.obj.altdriver, self.obj.driver)
        self.quests.select_quest(object_name, quest_name)
        