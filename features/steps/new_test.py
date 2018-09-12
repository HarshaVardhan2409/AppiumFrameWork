'''import os
import sys
from time import sleep

from altunityrunner import AltrunUnityDriver
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



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
    desired_caps['app'] = 'C:\\Users\\Automation\\Downloads\\New folder\\automation_package_30_08_2018_2\\cars.apk'
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
action = ActionChains(driver);
action.send_keys('cars_evening_the_odds_v7').perform()
sleep(5)
#driver.find_element(By.XPATH, '//android.widget.Button[@text="OK"]').click()
driver.find_element_by_xpath('//android.widget.Button[@text="OK"]').click()



#altdriver.stop()
#driver.quit()
'''