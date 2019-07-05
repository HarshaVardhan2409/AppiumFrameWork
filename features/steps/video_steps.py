from time import sleep
import sys
import os
from selenium.webdriver.common.by import By

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


sys.path.append(PATH('../app/'))
from video import Video

sys.path.append(PATH('../../generics/'))
import constants
import generics_lib

sys.path.append(PATH('./'))
from generic_steps import GenericStep

class VideoSteps(GenericStep):
    
    video = None
    
    @step('forward the video to duration: "{duration}"')
    def forward_video(self, duration):
        self.video = Video(self.obj.altdriver, self.obj.driver)
        self.video.forward_video(float(duration))
        
    @step('verify the video at duration: "{duration}"')
    def verify_video(self, duration):
        self.video = Video(self.obj.altdriver, self.obj.driver)
        self.video.verify_video(float(duration))

    @step('forward the video to end')
    def forward_video_end(self):
        self.video = Video(self.obj.altdriver, self.obj.driver)
#         self.video.forward_video_end()
        self.video.scroll_video_end('Interstitial/FadeTransition-Loading', 'Tasks')
    
    @step('forward the library video to end')
    def forward_library_video_end(self):
        self.video = Video(self.obj.altdriver, self.obj.driver)
#         self.video.forward_video_end()
        self.video.scroll_video_end('Interstitial/FadeTransition-Loading', 'Library')
        
    @step('navigate back from video')
    def video_back(self):
        self.video = Video(self.obj.altdriver, self.obj.driver)
        self.video.video_back()
    
    @step('forward the video to 80% of the total duration')
    def forward_80(self):
        self.video = Video(self.obj.altdriver, self.obj.driver)
        self.video.forward_video_percentage(80)
        
    @step('forward the video to 85% of the total duration')
    def forward_85(self):
        self.video = Video(self.obj.altdriver, self.obj.driver)
        self.video.forward_video_percentage(85)
        
    @step('forward the video to duration and select the option')
    def forward_video_select_correct_option(self):
        self.video = Video(self.obj.altdriver, self.obj.driver)
        for row in self.table:
            self.video.forward_video_select_option(float(row['duration']), str(row['option_text']), str(row['acceptable']))
    
    @step('fast forward the video for "{count}" times and check')
    def fast_forward(self, count):
        self.video = Video(self.obj.altdriver, self.obj.driver)
        self.video.fast_forward_video(int(count))
        
    @step('rewind the video for "{count}" times and check')
    def rewind_video(self, count):
        self.video = Video(self.obj.altdriver, self.obj.driver)
        self.video.rewind_video(int(count))
        
    @step('check if video is paused')
    def check_pause(self):
        self.obj.driver.find_element(By.ID, "com.byjus.k3:id/exo_play")
        
    @step('resume the video')
    def resume(self):
        self.obj.driver.find_element(By.ID, "com.byjus.k3:id/exo_play").click()

