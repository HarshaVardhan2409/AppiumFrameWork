import os
import sys
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../games/templates/'))
from base_class import BaseClass

class Onboarding(BaseClass):
    
    def verify_country_images(self, object_name, image_name):
        country_name = self.altdriver.wait_for_element(object_name).get_component_property("UnityEngine.UI.Image", "sprite")
        assert image_name in country_name
        
    def verify_country_details(self, country_name):
        sleep(1)
        name = self.get_text('Label')
        image = self.altdriver.wait_for_element('CountryIcon').get_component_property("UnityEngine.UI.Image", "sprite")
        code = self.get_text('CountryCode')
        
        country_images = {"India":"India", "Bahrain":"Bahrain", "UAE":"UAE", "Kuwait":"Kuwait", "Oman":"Oman", "Qatar":"Qatar", "Saudi Arabia":"SaudiArabia"}
        country_codes = {"India":"+91", "Bahrain":"+973", "UAE":"+971", "Kuwait":"+965", "Oman":"+968", "Qatar":"+974", "Saudi Arabia":"+966"}
        assert country_name in name
        assert country_images[str(country_name)] in image
        assert country_codes[str(country_name)] in str(code)
            