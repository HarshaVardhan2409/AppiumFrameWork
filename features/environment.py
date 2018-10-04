from __builtin__ import str
import os
import subprocess
import sys
from time import sleep

from steps.base_setup import BaseSetup

sys.path.append('../generics/')
import test_management
        
obj = BaseSetup()

def before_all(context):
    BaseSetup.app_path = str(context.config.userdata['APP_PATH'])
    device_type = str(context.config.userdata['DEVICE_TYPE'])
    BaseSetup.platform = device_type
    
    test_management.testrail_username = str(context.config.userdata['TESTRAIL_USER'])
    test_management.testrail_password = str(context.config.userdata['TESTRAIL_PASS'])
    
    if 'android' in device_type:
        subprocess.Popen('adb forward tcp:13001 tcp:13000', shell=True)
    elif 'ios' in device_type:
        subprocess.Popen('iproxy forward tcp:13001 tcp:13000', shell=True)
    subprocess.Popen('appium', shell=True)
    sleep(40)
    context.obj = obj
    context.obj.setup()

def after_scenario(context, scenario):
    context.obj = obj
    
    data = None
    data = str(context.scenario)
    data = data.split('">')
    data = data[0].split('_')
    data.reverse()
    
    if context.failed:
        directory = '%s/' % os.getcwd()
        file_name = 'screen.png'
        context.obj.driver.save_screenshot(directory + file_name)
        
        test_management.update_testrail(data[1], data[0] , False, 'Test case failed')
    else:
        test_management.update_testrail(data[1], data[0] , True, 'Test case passed')
    
    context.obj.relaunch_app()

def after_all(context):
    
    context.obj = obj
    context.obj.teardown()
    
    try:
        # Use below code to Stop appium server on the local windows machine
        subprocess.Popen('Taskkill /IM node.exe /F',shell=True)
    except:
        # Use below code to stop appium server on the local mac machine
        subprocess.Popen('Taskkill /IM node.exe /F',shell=True)
