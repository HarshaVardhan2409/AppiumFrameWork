from appium import webdriver
from altunityrunner import AltrunUnityDriver

class Base_Setup():
    altdriver = None
    driver = None
    platform = 'android'  # set to `ios` or `android` to change platform
    app_path = None
    
    def setup(self):
        self.desired_caps = {}
        if ("android" in self.platform.lower()):
            self.setup_android()
        elif ("ios" in self.platform.lower()):
            self.setup_ios()
        else:
            print 'platform do not match'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
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

