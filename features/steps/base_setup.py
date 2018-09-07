from altunityrunner import AltrunUnityDriver
from appium import webdriver
import sys

sys.path.append('../generics/')
import generics_lib
import constants


#from ...generics import generics_lib, constants
class BaseSetup():
    altdriver = None
    driver = None
    platform = None  # set to `ios` or `android` to change platform
    app_path = None
    
    def setup(self):
        self.desired_caps = {}
        if ("android" in self.platform.lower()):
            self.setup_android()
        elif ("ios" in self.platform.lower()):
            self.setup_ios()
        else:
            print 'platform do not match'
            
        ip_address = generics_lib.get_data(constants.config_path, 'appium_server', 'ip_address')
        port = generics_lib.get_data(constants.config_path, 'appium_server', 'port')
        self.driver = webdriver.Remote('http://'+ip_address+':'+port+'/wd/hub', self.desired_caps)
        self.altdriver = AltrunUnityDriver(self.driver, self.platform)

    def teardown(self):
        self.altdriver.stop()
        self.driver.quit()

    def setup_android(self):
        self.desired_caps['platformName'] = 'android'
        self.desired_caps['deviceName'] = 'device'
        self.desired_caps['app'] = self.app_path

    # This will be handled with iOS implementation.
    def setup_ios(self):
        self.desired_caps['platformName'] = 'iOS'
        self.desired_caps['deviceName'] = 'device'
        self.desired_caps['automationName'] = 'XCUITest'
        self.desired_caps['app'] = self.app_path
        
    def relaunch_app(self):
        self.driver.launch_app()
