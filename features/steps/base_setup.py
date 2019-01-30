from altunityrunner import AltrunUnityDriver
from appium import webdriver
import sys
import os
from selenium.webdriver.common.by import By

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../../generics/'))
import generics_lib
import constants

class BaseSetup():
    altdriver = None
    driver = None
    platform = None  # set to `ios` or `android` to change platform
    system_os = None
    app_path = None
    desired_caps = None
    ip_address = None
    port = None
    
    def install_app(self):
        self.desired_caps = {}
        if ("android" in self.platform.lower()):
            self.setup_android()
        elif ("ios" in self.platform.lower()):
            self.setup_ios()
        else:
            print 'platform do not match'
            
        self.ip_address = generics_lib.get_data(constants.CONFIG_PATH, 'appium_server', 'ip_address')
        self.port = generics_lib.get_data(constants.CONFIG_PATH, 'appium_server', 'port')
        self.driver = webdriver.Remote('http://'+self.ip_address+':'+self.port+'/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(15)
        
        self.altdriver = AltrunUnityDriver(self.driver, self.platform)

    def teardown(self):
        self.altdriver.stop()
        self.driver.quit()

    def setup_android(self):
        self.desired_caps['platformName'] = 'android'
        self.desired_caps['deviceName'] = 'device'
        self.desired_caps['app'] = self.app_path
        self.desired_caps['newCommandTimeout'] = 300

    # This will be handled with iOS implementation.
    def setup_ios(self):
        self.desired_caps['platformName'] = 'iOS'
        self.desired_caps['deviceName'] = 'device'
        self.desired_caps['automationName'] = 'XCUITest'
        self.desired_caps['app'] = self.app_path
        self.desired_caps['newCommandTimeout'] = 300
        
    def launch_app(self, appPackage, appActivity, noreset_status):
        self.desired_caps = {}
        if 'android' in self.platform:
            self.desired_caps['platformName'] = 'android'
            self.desired_caps['deviceName'] = 'device'
            self.desired_caps['newCommandTimeout'] = 300
            if 'rue' in noreset_status:
                noreset_status = True
            elif 'alse' in noreset_status:
                noreset_status = False
            self.desired_caps['noReset'] = noreset_status
            self.desired_caps['appPackage'] = appPackage
            self.desired_caps['appActivity'] = appActivity
            self.ip_address = generics_lib.get_data(constants.CONFIG_PATH, 'appium_server', 'ip_address')
            self.port = generics_lib.get_data(constants.CONFIG_PATH, 'appium_server', 'port')
            self.driver = webdriver.Remote('http://'+self.ip_address+':'+self.port+'/wd/hub', self.desired_caps)
            self.driver.implicitly_wait(15)
            self.altdriver = AltrunUnityDriver(self.driver, self.platform)
        