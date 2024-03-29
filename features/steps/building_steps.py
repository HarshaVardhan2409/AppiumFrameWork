from time import sleep
import sys
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../app/'))
from buildings import Buildings
from stickerbook import StickerBook

sys.path.append(PATH('../../generics/'))
import constants
import generics_lib

sys.path.append(PATH('./'))
from generic_steps import GenericStep

class BuildingSteps(GenericStep):
    
    buildings = None
    sticker_book = None
    
    @step('tap on building "{building_name}"')
    def select_building(self, building_name):
        self.buildings = Buildings(self.obj.altdriver, self.obj.driver)
        self.buildings.select_building('Building_', building_name)
        
    @step('navigate back from task scene')
    def back_tasks(self):
        self.base_class.tap('BackButton')
        
    @step('quest is loaded')
    def quests_loaded(self):
        self.buildings = Buildings(self.obj.altdriver, self.obj.driver)
        self.base_class.wait_for_scene('Quests')
        self.base_class.wait_for_element_not_present('Interstitial/FadeTransition-Loading')
        self.base_class.wait_for_element_display('BackButton')
        sleep(2)
        
    @step('verify the quest progression')
    def quests_progression(self):
        self.buildings = Buildings(self.obj.altdriver, self.obj.driver)
        self.buildings = Buildings(self.obj.altdriver, self.obj.driver)
        self.base_class.wait_for_scene('Quests')
        self.base_class.wait_for_element_not_present('Interstitial/FadeTransition-Loading')
        for row in self.table:
            self.buildings.scroll_verify_quest(row['quest_name'])
            self.buildings.verify_quest_progression('QuestItem ', row['quest_name'], row['total_tasks'], row['completed_tasks'])

    @step('tap on quest "{quest_name}"')
    def select_quest(self, quest_name):
        self.buildings = Buildings(self.obj.altdriver, self.obj.driver)
        self.buildings.select_quest('Task Name', quest_name)
        
    @step('task is loaded')
    def tasks_loaded(self):
        self.buildings = Buildings(self.obj.altdriver, self.obj.driver)
        self.base_class.wait_for_scene('Tasks')
        self.base_class.wait_for_element_not_present('Interstitial/FadeTransition-Loading')
        self.base_class.wait_for_element_display('BackButton')
        sleep(2)

    @step('tap on task "{task_number}"')
    def select_task_video(self, task_number):
        self.buildings = Buildings(self.obj.altdriver, self.obj.driver)
        self.buildings.select_task('TaskCard_', int(task_number))

    @step('scroll and verify the buildings')
    def verify_specific_building(self):
        self.buildings = Buildings(self.obj.altdriver, self.obj.driver)
        for row in self.table:
            self.buildings.scroll_verify_building(row['building_name'])

    @step('scroll and verify the quests')
    def verify_specific_quest(self):
        self.buildings = Buildings(self.obj.altdriver, self.obj.driver)
        for row in self.table:
            self.buildings.scroll_verify_quest(row['quest_name'])

    @step('game is launched "{game_name}"')
    def game_loaded(self, game_name):
        self.buildings = Buildings(self.obj.altdriver, self.obj.driver)
        self.base_class.wait_for_scene(game_name)
        
    @step('game is completed')
    def game_completed(self):
        self.base_class.wait_for_scene('Tasks')
        self.base_class.wait_for_element_not_present('Interstitial/FadeTransition-Loading')

    @step('verify the stickers from quest')
    def verify_stickers_quest(self):
        self.buildings = Buildings(self.obj.altdriver, self.obj.driver)
        self.sticker_book = StickerBook(self.obj.altdriver, self.obj.driver)
        self.base_class.wait_for_scene('Quests')
        self.base_class.verify_the_element_on_screen('gift_box')
        sticker_names = self.buildings.get_sticker_names()
        print "+++++++++++========================++++++++++++++++++"
        print sticker_names
        self.base_class.tap('gift_box_icon')
        self.base_class.wait_for_element_not_present('gift_box')
        self.base_class.tap('Stickerbook')
        self.base_class.wait_for_scene('stickerbook')
        self.base_class.wait_for_element_display('OpenDoodle')
        for i in range(len(sticker_names)):
            self.sticker_book.check_sticker(sticker_names[i])
            
        
    
        
        
        