'''import os
from time import sleep

from altunityrunner import AltrunUnityDriver
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import sys
sys.path.append('../generics/')
import generics_lib


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

altdriver = None
driver = None
platform = "android"  # set to `ios` or `android` to change platform

desired_caps = {}
if (platform == "android"):
    desired_caps['platformName'] = 'android'
    desired_caps['deviceName'] = 'device'
    desired_caps['app'] = PATH('../../../cars.apk')
else:
    desired_caps['platformName'] = 'iOS'
    desired_caps['deviceName'] = 'iPhone5'
    desired_caps['automationName'] = 'XCUITest'
    desired_caps['app'] = PATH('../../../sampleGame.ipa')
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
altdriver = AltrunUnityDriver(driver, platform)

altdriver.wait_for_current_scene_to_be('AutomationScene')
sleep(5)
altdriver.wait_for_element('InputField').tap()
sleep(5)
generics_lib.action_SendKeys(driver, 'cars_evening_the_odds_v7')
driver.press_keycode()


#altdriver.stop()
#driver.quit()

'''