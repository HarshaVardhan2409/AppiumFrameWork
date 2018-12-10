from time import sleep
import sys
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../app/'))
from onboarding import Onboarding

sys.path.append(PATH('../../generics/'))
import constants
import generics_lib

sys.path.append(PATH('./'))
from generic_steps import GenericStep

class OnboardingSteps(GenericStep):
    
    onboarding = None
    
    @step('verify the country images')
    def verify_country_images(self):
        self.onboarding = Onboarding(self.obj.altdriver, self.obj.driver)
        #wait dropdown
        sleep(2)
        for row in self.table:
            self.onboarding.verify_country_images(row['object_name'], row['image_name'])
            
    @step('verify the country name, national flag and country code for: "{country_name}"')
    def verify_country_details(self, country_name):
        self.onboarding = Onboarding(self.obj.altdriver, self.obj.driver)
        self.onboarding.verify_country_details(country_name)
        
    