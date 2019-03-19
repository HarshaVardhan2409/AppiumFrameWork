import os
import sys
from time import sleep
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../games/templates/'))
from base_class import BaseClass

sys.path.append(PATH('../../generics'))
import generics_lib

class Video(BaseClass):
    
    def forward_video(self, duration):
        self.action = TouchAction(self.driver)
        sleep(3)
        dSize = (self.driver.get_window_size())
        x = (dSize['width']*0.8)
        y = (dSize['height']*0.8)
        self.action.tap(x = x, y = y).perform()
        while float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.')) == 0.0:
            self.action.tap(x = x, y = y).perform()
            self.action.tap(x = x, y = y).perform()
        sleep(3)
        flag = True
        while flag == True:
            try:
                self.driver.implicitly_wait(1)
                self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration")
                self.driver.implicitly_wait(20)
                flag = False
            except:
                self.action.tap(x = x, y = y).perform()
                flag = True
#         duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.'))

        element = self.driver.find_element(By.ID, "com.byjus.k3:id/exo_progress")
        
        location =  element.location
        size = element.size
        self.driver.find_element(By.ID, "com.byjus.k3:id/exo_pause").click()
        x = (location['x'] + (size['width']))
        y = (location['y'] + (size['height']/2))
        x2 = location['x']
        current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
        total_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.'))
        percentage = 0
        default = 0
        value = 0
        change = 0
        if duration <= total_duration:
            minutes = (int(str(duration).split('.')[0])*60)
            seconds = (int(str("%.2f" % duration).split('.')[1]))
            change = size['width']/((int(str(total_duration).split('.')[0])*60) + (int(str("%.2f" % total_duration).split('.')[1])))
            
            dur = (minutes + seconds) * change
            value = default + dur
            percentage = x2 + value
            self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
            x2 = percentage
            
            self.action.tap(x = x, y = y).perform()
            current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
            first = (minutes + seconds)
            while current_duration != duration:
                second = ((int(str(current_duration).split('.')[0])*60) + (int(str("%.2f" % current_duration).split('.')[1])))
                if current_duration < duration:
                    diff = first - second
                    percentage = x2 + (change * diff)
                    self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
                    x2 = percentage
                    self.action.tap(x = x, y = y).perform()
                elif current_duration > duration:
                    diff = second - first
                    percentage = x2 - (change * diff)
                    self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
                    x2 = percentage
                    self.action.tap(x = x, y = y).perform()
                if diff == 1 or diff == 2:
                    break
                else:
                    try:
                        self.driver.implicitly_wait(5)
                        current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
                        self.driver.implicitly_wait(20)
                    except:
                        self.driver.implicitly_wait(20)
                        break
        else:
            print 'Given duration is out of total duration.........'


    def verify_video(self, duration=0):
        self.action = TouchAction(self.driver)
        sleep(3)
        dSize = (self.driver.get_window_size())
        x = (dSize['width']*0.8)
        y = (dSize['height']*0.8)
        while float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.')) == 0.0:
            sleep(1)
            self.action.tap(x = x, y = y).perform()
            self.action.tap(x = x, y = y).perform()
        
        element = self.driver.find_element(By.ID, "com.byjus.k3:id/exo_progress")
        location =  element.location
        size = element.size

        x = (location['x'] + (size['width']))
        y = (location['y'] + (size['height']/2))
        x2 = location['x']
        current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
        total_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.'))
        print total_duration
        percentage = 0
        default = 0
        value = 0
        change = 0
        if duration <= total_duration:
            minutes = (int(str(duration).split('.')[0])*60)
            seconds = (int(str("%.2f" % duration).split('.')[1]))
            change = size['width']/((int(str(total_duration).split('.')[0])*60) + (int(str("%.2f" % total_duration).split('.')[1])))
            
            dur = (minutes + seconds) * change
            value = default + dur
            percentage = x2 + value
            self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
            x2 = percentage
            current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
            first = (minutes + seconds)
            while current_duration != duration:
                second = ((int(str(current_duration).split('.')[0])*60) + (int(str("%.2f" % current_duration).split('.')[1])))
                if current_duration < duration:
                    diff = first - second
                    percentage = x2 + (change * diff)
                    self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
                    x2 = percentage
                elif current_duration > duration:
                    diff = second - first
                    percentage = x2 - (change * diff)
                    self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
                    x2 = percentage
                if diff == 1 or diff == 2:
                    self.driver.find_element(By.ID, "com.byjus.k3:id/exo_pause").click()
                    self.action.tap(x = x, y = y).perform()
                    break
                else:
                    current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
        else:
            print 'Given duration is out of total duration.........' 
        sleep(3)
        directory = PATH('../../compare_images/actual_image.png')
        generics_lib.takescreenshot(self.driver, directory)
        directory2 = PATH('../../compare_images/expected_image.png')
        score = generics_lib.compare_video_images(directory2, directory)
        assert score > 80


    def forward_video_end(self):
        self.action = TouchAction(self.driver)
        sleep(3)
        dSize = (self.driver.get_window_size())
        x = (dSize['width']*0.8)
        y = (dSize['height']*0.8)
        duration = 0
        self.action.tap(x = x, y = y).perform()
        while float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.')) == 0.0:
            self.action.tap(x = x, y = y).perform()
            self.action.tap(x = x, y = y).perform()
        sleep(3)
        flag = True
        while flag == True:
            try:
                self.driver.implicitly_wait(1)
                self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration")
                self.driver.implicitly_wait(20)
                flag = False
            except:
                self.action.tap(x = x, y = y).perform()
                flag = True
        duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.'))

        element = self.driver.find_element(By.ID, "com.byjus.k3:id/exo_progress")
        location =  element.location
        size = element.size

        x = (location['x'] + (size['width']))
        y = (location['y'] + (size['height']/2))
        x2 = location['x']
        current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
        total_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.'))
        percentage = 0
        default = 0
        value = 0
        change = 0
        if duration <= total_duration:
            minutes = (int(str(duration).split('.')[0])*60)
            seconds = (int(str("%.2f" % duration).split('.')[1]))
            change = size['width']/((int(str(total_duration).split('.')[0])*60) + (int(str("%.2f" % total_duration).split('.')[1])))
            
            dur = (minutes + seconds) * change
            value = default + dur
            percentage = x2 + value
            self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
            x2 = percentage
            
            self.action.tap(x = x, y = y).perform()
            current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
            first = (minutes + seconds)
            while current_duration != duration:
                second = ((int(str(current_duration).split('.')[0])*60) + (int(str("%.2f" % current_duration).split('.')[1])))
                if current_duration < duration:
                    diff = first - second
                    percentage = x2 + (change * diff)
                    self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
                    x2 = percentage
                    self.action.tap(x = x, y = y).perform()
                elif current_duration > duration:
                    diff = second - first
                    percentage = x2 - (change * diff)
                    self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
                    x2 = percentage
                    self.action.tap(x = x, y = y).perform()
                if diff == 1 or diff == 2:
                    break
                else:
                    try:
                        self.driver.implicitly_wait(5)
                        current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
                        self.driver.implicitly_wait(20)
                    except:
                        self.driver.implicitly_wait(20)
                        break
        else:
            print 'Given duration is out of total duration.........'

