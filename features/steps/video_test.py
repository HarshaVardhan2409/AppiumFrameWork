# -*- coding: utf-8 -*-

from altunityrunner.runner import AltrunUnityDriver
from appium import webdriver
from time import sleep
import sys
from ast import literal_eval
import os

from appium.webdriver.connectiontype import ConnectionType
import json
from decimal import Decimal
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../../generics/'))
import constants
import generics_lib

driver = None
def launch_app(platform, duration=0, pause=0):
    desired_caps = {}
    if 'android' in platform:
        desired_caps['platformName'] = 'android'
        desired_caps['deviceName'] = 'device'
        desired_caps['newCommandTimeout'] = 300
        desired_caps['noReset'] = True
        desired_caps['appPackage'] = "com.byjus.support" #"com.byjus.k3" 
        desired_caps['appActivity'] = "com.byjus.support.MainActivity" #"com.byjus.unity.support.activities.MainActivity" #
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(15)
        print 'navigate to video....................'
        #sleep(60)
        print 'starting ...........'
        sleep(3)
        driver.orientation = 'LANDSCAPE'
        sleep(4)
        driver.find_element(By.ID, "com.byjus.support:id/playVideoButton").click()
        sleep(6)
        driver.find_element(By.ID, "com.byjus.support:id/playVideoButton").click()
        driver.find_element(By.ID, "com.byjus.support:id/playVideoButton").click()
        sleep(2)
        element = driver.find_element(By.ID, "com.byjus.support:id/exo_progress")
        location =  element.location
        size = element.size
        print location
        print size
        action = TouchAction(driver)
        x = (location['x'] + (size['width']))
        y = (location['y'] + (size['height']/2))
        print x
        print y
        x2 = location['x']
        y2 = (location['y'] + (size['height']/2))
        current_duration = float(driver.find_element(By.ID, "com.byjus.support:id/exo_position").text.replace(':', '.'))
        #current_duration = current_duration.replace(':', '.')
        #current_duration = float(current_duration)
        total_duration = float(driver.find_element(By.ID, "com.byjus.support:id/exo_duration").text.replace(':', '.'))
        #total_duration = total_duration.replace(':', '.')
        #total_duration = float(total_duration)
        
        count = 0
        percentage = 0
        default = 13.6
        value = 0
        if duration <= total_duration:
            print duration
            minutes = (int(str(duration).split('.')[0])*60)
            seconds = (int(str("%.2f" % duration).split('.')[1]))
            print minutes
            print seconds
            dur = (minutes + seconds) * 0.2
            print '--------------'
            print dur
            value = default + dur
            percentage = (x*(value))/100
            action.press(x =  x2, y = y2).wait(3000).move_to(x = percentage, y = y).release().perform()
            x2 = percentage
            current_duration = driver.find_element(By.ID, "com.byjus.support:id/exo_position").text
            current_duration = current_duration.replace(':', '.')
            current_duration = float(current_duration)
            print duration
            while current_duration != duration:
                if current_duration < duration:
                    count = 0.2
                    value = value + count
                    percentage = (x*(value))/100
                    print percentage
                    action.press(x =  x2, y = y2).wait(2500).move_to(x = percentage, y = y).release().perform()
                    x2 = percentage
                elif current_duration > duration:
                    value = value - 0.2
                    percentage = (x*(value))/100
                    action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
                    x2 = percentage
                current_duration = driver.find_element(By.ID, "com.byjus.support:id/exo_position").text
                current_duration = current_duration.replace(':', '.')
                current_duration = float(current_duration)
                
        else:
            print 'Given duration is out of total duration.........'
        
        
        driver.find_element(By.ID, "com.byjus.support:id/playVideoButton").click()
        driver.find_element(By.ID, "700 ml").click()
        sleep(2)
        directory = 'C:\\Users\\Vinayaka\\Downloads\\correct2.png'
        driver.save_screenshot(directory)
        assert generics_lib.compare_video_images("C:\\Users\\Vinayaka\\Downloads\\correct1.png", "C:\\Users\\Vinayaka\\Downloads\\correct2.png") > 80
        """
        driver.find_element(By.ID, "com.byjus.support:id/playVideoButton").click()
        current_duration = driver.find_element(By.ID, "com.byjus.support:id/exo_position").text
        current_duration = current_duration.replace(':', '.')
        current_duration = float(current_duration)
        count = 0
        while pause != current_duration:
            sleep(0.9)
            driver.find_element(By.ID, "com.byjus.support:id/playVideoButton").click()
            current_duration = driver.find_element(By.ID, "com.byjus.support:id/exo_position").text
            current_duration = current_duration.replace(':', '.')
            current_duration = float(current_duration)
            if pause == current_duration:
                break
            driver.find_element(By.ID, "com.byjus.support:id/playVideoButton").click()
        action.tap(x= 450, y = 500).perform()
        directory = 'C:\\Users\\Vinayaka\\Downloads\\pause1.png'
        driver.save_screenshot(directory)
        assert generics_lib.compare_video_images("C:\\Users\\Vinayaka\\Downloads\\pause1.png", "C:\\Users\\Vinayaka\\Downloads\\pause2.png") > 70
        """
        #action.tap(x = x, y = y).perform()
    
#launch_app('android', 03.30, 2.44)

