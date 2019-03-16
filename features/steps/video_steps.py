from time import sleep
import sys
import os

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
        self.video.forward_video_end()

