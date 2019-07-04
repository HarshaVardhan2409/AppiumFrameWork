import os
import sys
from time import sleep
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import subprocess
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

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
        self.wait_video_controls()
        dSize = (self.driver.get_window_size())
        x = (dSize['width']*0.8)
        y = (dSize['height']*0.8)
        self.wait_video_controls()
        while float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.')) == 0.0:
            self.action.tap(x = x, y = y).perform()
            self.action.tap(x = x, y = y).perform()
        self.wait_video_controls()
        self.driver.find_element(By.ID, "com.byjus.k3:id/exo_pause").click()
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
            self.wait_video_controls()
            try:
                self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
            except:
                scroll_values = 'adb shell input touchscreen swipe '+str(x2)+' '+str(y)+' '+str(percentage)+' '+str(y)
                print '=================================scroll================='
                print scroll_values
                os.system(scroll_values)
            x2 = percentage
            self.wait_video_controls()
            current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
            first = (minutes + seconds)
            while current_duration != duration:
                self.wait_video_controls()
                current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
                second = ((int(str(current_duration).split('.')[0])*60) + (int(str("%.2f" % current_duration).split('.')[1])))
                if current_duration < duration:
                    diff = first - second
                    percentage = x2 + (change * diff)
                    try:
                        self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
                    except:
                        scroll_values = 'adb shell input touchscreen swipe '+str(x2)+' '+str(y)+' '+str(percentage)+' '+str(y)
                        print '=================================scroll================='
                        print scroll_values
                        os.system(scroll_values)
                    x2 = percentage
                elif current_duration > duration:
                    diff = second - first
                    percentage = x2 - (change * diff)
                    try:
                        self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
                    except:
                        scroll_values = 'adb shell input touchscreen swipe '+str(x2)+' '+str(y)+' '+str(percentage)+' '+str(y)
                        print '=================================scroll================='
                        print scroll_values
                        os.system(scroll_values)
                    x2 = percentage
                if diff < 5:
                    break
        else:
            assert  duration <= total_duration, 'forward duration ' + duration + ' is more than total duration ' + total_duration


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
        score = generics_lib.pixel_comparision(directory2, directory)
        assert score > 80


    def forward_video_end(self):
        self.action = TouchAction(self.driver)
        self.wait_video_controls()
        dSize = (self.driver.get_window_size())
        x = (dSize['width']*0.8)
        y = (dSize['height']*0.8)
        duration = 0
        self.wait_video_controls()
        while float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.')) == 0.0:
            self.action.tap(x = x, y = y).perform()
            self.action.tap(x = x, y = y).perform()
        self.wait_video_controls()
        self.driver.find_element(By.ID, "com.byjus.k3:id/exo_pause").click()
        duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.')) - (0.05)
        if duration > 5.3:
            duration = duration - 0.03
        if '.9' in str(duration):
            duration = duration - 0.40    
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
        count = 0
        if duration <= total_duration:
            minutes = (int(str(duration).split('.')[0])*60)
            seconds = (int(str("%.2f" % duration).split('.')[1]))
            change = size['width']/((int(str(total_duration).split('.')[0])*60) + (int(str("%.2f" % total_duration).split('.')[1])))
            
            dur = (minutes + seconds) * change
            value = default + dur
            percentage = x2 + value
            self.wait_video_controls()
            self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
            x2 = percentage
            self.wait_video_controls()
            current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
            first = (minutes + seconds)
            if current_duration == duration or str(current_duration) in str(duration):
                self.wait_video_controls()
                print "====================================="
                print 'clicked play.................'
                self.driver.find_element(By.ID, "com.byjus.k3:id/exo_play").click()
                sleep(10)
            while current_duration != duration and count < 20:
                count += 1
                self.wait_video_controls()
                current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
                second = ((int(str(current_duration).split('.')[0])*60) + (int(str("%.2f" % current_duration).split('.')[1])))
                if current_duration < duration:
                    print 'entering current less than duration'
                    diff = first - second
                    percentage = x2 + (change * diff)
                    self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
                    x2 = percentage
                elif current_duration > duration:
                    print 'entering current more than duration'
                    diff = second - first
                    percentage = x2 - (change * diff)
                    self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
                    x2 = percentage
                self.wait_video_controls()
                current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
                self.wait_video_controls()
                print "Duration................."
                print current_duration
                print duration
                if current_duration == duration or str(current_duration) in str(duration):
                    self.wait_video_controls()
                    print "====================================="
                    print 'clicked play...............'
                    self.driver.find_element(By.ID, "com.byjus.k3:id/exo_play").click()
                    break
        else:
            assert  duration <= total_duration, 'forward duration ' + duration + ' is more than total duration ' + total_duration
            
    def forward_video_percentage(self, scroll_percentage):
        self.action = TouchAction(self.driver)
        dSize = (self.driver.get_window_size())
        x = (dSize['width']*0.8)
        y = (dSize['height']*0.8)
        self.wait_video_controls()
        while float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.')) == 0.0:
            self.action.tap(x = x, y = y).perform()
            self.action.tap(x = x, y = y).perform()
        self.wait_video_controls()
        self.driver.find_element(By.ID, "com.byjus.k3:id/exo_pause").click()
        total_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.'))
        element = self.driver.find_element(By.ID, "com.byjus.k3:id/exo_progress")
        location =  element.location
        size = element.size
        x = (location['x'] + (size['width']))
        y = (location['y'] + (size['height']/2))
        x2 = location['x']
        percentage = 0
        default = 0
        value = 0
        change = 0
        count = 0
        total_seconds = (int(str(total_duration).split('.')[0])*60) + (int(str("%.2f" % total_duration).split('.')[1]))
        scroll_seconds = int((total_seconds*scroll_percentage)/100)
        print "checking video 80 scroll......................."
        print total_seconds
        print scroll_seconds
        if scroll_seconds < total_seconds:
            change = size['width']/(total_seconds)
            dur = scroll_seconds * change
            value = default + dur
            percentage = x2 + value
            current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
            current_seconds = (int(str(current_duration).split('.')[0])*60) + (int(str("%.2f" % current_duration).split('.')[1]))
            print current_seconds
            while current_seconds != scroll_seconds and count < 20:
                count += 1
                self.wait_to_load()
                current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
                current_seconds = ((int(str(current_duration).split('.')[0])*60) + (int(str("%.2f" % current_duration).split('.')[1])))
                if current_seconds < scroll_seconds:
                    print 'entering current less than expected'
                    diff = scroll_seconds - current_seconds
                    percentage = x2 + (change * diff)
                    try:
                        self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
                    except:
                        scroll_values = 'adb shell input touchscreen swipe '+str(x2)+' '+str(y)+' '+str(percentage)+' '+str(y)
                        print '=================================scroll================='
                        print scroll_values
                        os.system(scroll_values)
                    x2 = percentage
                elif current_seconds > scroll_seconds:
                    print 'entering current more than expected'
                    diff = current_seconds - scroll_seconds
                    percentage = x2 - (change * diff)
                    try:
                        self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
                    except:
                        scroll_values = 'adb shell input touchscreen swipe '+str(x2)+' '+str(y)+' '+str(percentage)+' '+str(y)
                        print '=================================scroll================='
                        print scroll_values
                        os.system(scroll_values)
                    x2 = percentage
                self.wait_to_load()
                current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
                current_seconds = ((int(str(current_duration).split('.')[0])*60) + (int(str("%.2f" % current_duration).split('.')[1])))
                self.wait_to_load()
                print "Duration................."
                print current_seconds
                if current_seconds == scroll_seconds or str(current_seconds) in str(scroll_seconds):
                    break
        else:
            assert  scroll_seconds < total_seconds, 'forward duration ' + scroll_seconds + ' is more than total duration ' + total_seconds
    
    def scroll_video_end(self, object_name, scene_name):
        self.action = TouchAction(self.driver)
        self.altdriver.wait_for_current_scene_to_be(scene_name)
        self.altdriver.wait_for_element(object_name)
        self.wait_video_controls()
        dSize = (self.driver.get_window_size())
        x = (dSize['width']*0.8)
        y = (dSize['height']*0.8)
        duration = 0
        self.wait_video_controls()
        while float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.')) == 0.0:
            self.action.tap(x = x, y = y).perform()
            self.action.tap(x = x, y = y).perform()
        self.wait_video_controls()
        self.driver.find_element(By.ID, "com.byjus.k3:id/exo_pause").click()
        element = self.driver.find_element(By.ID, "com.byjus.k3:id/exo_progress")
        location =  element.location
        size = element.size
        x = (location['x'] + (size['width']))
        y = (location['y'] + (size['height']/2))
        x2 = location['x']
        flag = True
        count = 0
        val = 0
        while flag and count < 10:
            print 'scrolling..............'
            self.altdriver.wait_for_element(object_name, timeout=1)
            try:
                self.action.press(x =  x2, y = y).wait(2500).move_to(x = x, y = y).release().perform()
            except:
                self.driver.scroll(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_progress"), self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration"))
            while val < 15:
                try:
                    self.altdriver.wait_for_element_to_not_be_present(object_name, timeout=1)
                    flag = False
                    val = 16
                except:
                    val += 1
            count += 1
        assert flag == False, 'Unable to complete video'
        
    def forward_video_select_option(self, duration, text, acceptable):
        self.action = TouchAction(self.driver)
        wait = WebDriverWait(self.driver, 10)
        self.wait_video_controls()
        dSize = (self.driver.get_window_size())
        x = (dSize['width']*0.8)
        y = (dSize['height']*0.8)
        self.wait_video_controls()
        while float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.')) == 0.0:
            self.action.tap(x = x, y = y).perform()
            self.action.tap(x = x, y = y).perform()
        self.wait_video_controls()
        self.driver.find_element(By.ID, "com.byjus.k3:id/exo_pause").click()
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
            self.wait_video_controls()
            try:
                self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
            except:
                scroll_values = 'adb shell input touchscreen swipe '+str(x2)+' '+str(y)+' '+str(percentage)+' '+str(y)
                print '=================================scroll================='
                print scroll_values
                os.system(scroll_values)
            x2 = percentage
            self.wait_video_controls()
            current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
            first = (minutes + seconds)
            while current_duration != duration:
                self.wait_video_controls()
                current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
                second = ((int(str(current_duration).split('.')[0])*60) + (int(str("%.2f" % current_duration).split('.')[1])))
                if current_duration < duration:
                    diff = first - second
                    percentage = x2 + (change * diff)
                    try:
                        self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
                    except:
                        scroll_values = 'adb shell input touchscreen swipe '+str(x2)+' '+str(y)+' '+str(percentage)+' '+str(y)
                        print '=================================scroll================='
                        print scroll_values
                        os.system(scroll_values)
                    x2 = percentage
                elif current_duration > duration:
                    diff = second - first
                    percentage = x2 - (change * diff)
                    try:
                        self.action.press(x =  x2, y = y).wait(2500).move_to(x = percentage, y = y).release().perform()
                    except:
                        scroll_values = 'adb shell input touchscreen swipe '+str(x2)+' '+str(y)+' '+str(percentage)+' '+str(y)
                        print '=================================scroll================='
                        print scroll_values
                        os.system(scroll_values)
                    x2 = percentage
                if diff < 5:
                    break
            self.wait_video_controls()
            self.driver.find_element(By.ID, "com.byjus.k3:id/exo_play").click()
            self.driver.find_element(By.ID, str(text)).click()
            if 'correct' == str(acceptable):
                wait.until(EC.invisibility_of_element(By.ID, str(text)))
            elif 'wrong' == str(acceptable):
                sleep(3)
                self.driver.find_element(By.ID, str(text))
        else:
            assert  duration <= total_duration, 'forward duration ' + str(duration) + ' is more than total duration ' + str(total_duration)
        
    def fast_forward_video(self, count):
        self.action = TouchAction(self.driver)
        dSize = (self.driver.get_window_size())
        x = (dSize['width']*0.8)
        y = (dSize['height']*0.8)
        self.wait_video_controls()
        while float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.')) == 0.0:
            self.action.tap(x = x, y = y).perform()
            self.action.tap(x = x, y = y).perform()
        self.wait_video_controls()
        current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
        total_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.'))
        total_sec = ((int(str(total_duration).split('.')[0])*60) + (int(str("%.2f" % total_duration).split('.')[1])))
        current_sec = ((int(str(current_duration).split('.')[0])*60) + (int(str("%.2f" % current_duration).split('.')[1])))
        diff_sec = float(total_sec) - float((current_sec + 2))
        possible_fwds = int(math.ceil(diff_sec/10))
        print '===============fast forward================'
        if count > possible_fwds:
            count = possible_fwds
        print diff_sec
        print possible_fwds
        print count
        switch = count
        while count > 0:
            self.wait_video_controls()
            self.driver.find_element(By.ID, "com.byjus.k3:id/exo_ffwd").click()
            count -= 1
        if switch == possible_fwds:
            self.altdriver.wait_for_element_to_not_be_present('Interstitial/FadeTransition-Loading')
        elif switch < possible_fwds:
            self.wait_video_controls()
            fwd_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
            fwd_sec = ((int(str(fwd_duration).split('.')[0])*60) + (int(str("%.2f" % fwd_duration).split('.')[1])))
            assert fwd_sec >= (current_sec + (switch * 10)) and (current_sec + (switch * 10) + 10)
            
    def rewind_video(self, count):
        self.action = TouchAction(self.driver)
        dSize = (self.driver.get_window_size())
        x = (dSize['width']*0.8)
        y = (dSize['height']*0.8)
        self.wait_video_controls()
        while float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration").text.replace(':', '.')) == 0.0:
            self.action.tap(x = x, y = y).perform()
            self.action.tap(x = x, y = y).perform()
        self.wait_video_controls()
        current_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
        current_sec = ((int(str(current_duration).split('.')[0])*60) + (int(str("%.2f" % current_duration).split('.')[1])))
        diff_sec = float((current_sec + 2))
        possible_rwds = int(math.ceil(diff_sec/10))
        print '===============rewinds================'
        if count > possible_rwds:
            count = possible_rwds
        switch = count
        while count > 0:
            self.wait_video_controls()
            self.driver.find_element(By.ID, "com.byjus.k3:id/exo_rew").click()
            count -= 1
        if switch == possible_rwds:
            self.wait_video_controls()
            rwd_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
            rwd_sec = ((int(str(rwd_duration).split('.')[0])*60) + (int(str("%.2f" % rwd_duration).split('.')[1])))
            assert rwd_sec < 10
        elif switch < possible_rwds:
            self.wait_video_controls()
            rwd_duration = float(self.driver.find_element(By.ID, "com.byjus.k3:id/exo_position").text.replace(':', '.'))
            rwd_sec = ((int(str(rwd_duration).split('.')[0])*60) + (int(str("%.2f" % rwd_duration).split('.')[1])))
            assert rwd_sec >= (current_sec - (switch * 10) - 10) and  rwd_sec <= (current_sec - (switch * 10) + 10)
            
        
    def video_back(self):
        self.wait_video_controls()
        self.driver.find_element(By.ID, "com.byjus.k3:id/back").click()
        sleep(1)
        self.altdriver.wait_for_element_to_not_be_present('Interstitial/FadeTransition-Loading')
        sleep(1)
        
    
    def wait_video_controls(self):
        self.action = TouchAction(self.driver)
        dSize = (self.driver.get_window_size())
        x = (dSize['width']*0.8)
        y = (dSize['height']*0.2)
        flag = True
        count = 0
        loading_count = 0
        while flag == True and count < 20:
            count += 1
            try:
                self.driver.implicitly_wait(0.5)
                try:
                    while self.driver.find_element(By.ID, "com.byjus.k3:id/exo_buffering").is_displayed() and loading_count < 75:
                        loading_count += 1
                        print 'Video loading present..................'
                        sleep(0.2)
                except:
                    print ''
                self.action.tap(x = x, y = y).perform()
                self.driver.find_element(By.ID, "com.byjus.k3:id/exo_duration")
                self.driver.implicitly_wait(20)
                flag = False
            except:
                loading_count = 0
                flag = True
        assert flag != True, "Video controls not displaying properly"
                
    def wait_to_load(self):
        loading_count = 0
        try:
            self.driver.implicitly_wait(0.5)
            while self.driver.find_element(By.ID, "com.byjus.k3:id/exo_buffering").is_displayed() and loading_count < 75:
                loading_count += 1
                print 'Video loading present..................'
                sleep(0.2)
            self.driver.implicitly_wait(20)
        except:
            self.driver.implicitly_wait(20)

