from __builtin__ import str
import os
import subprocess
import sys
from time import sleep

from steps.base_setup import BaseSetup

sys.path.append('../generics/')
import test_management

class Environment():
    
    case_num = None
    run_num = None
    
    def case_details(self, case, run):
        self.case_num = case
        self.run_num = run
        
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
    
    
    print context.table
    print context.text
    f = open('../features/test.text', "w+")
    f.write(str(context.table))
    f.close()
    f = open('../features/test2.text', "w+")
    f.write(str(context.text))
    f.close()
    if context.failed:
        directory = '%s/' % os.getcwd()
        file_name = 'screen.png'
        
        context.obj.driver.save_screenshot(directory + file_name)
        test_management.update_testrail(Environment.case_num, Environment.run_num , False, 'Test case failed')
    else:
        test_management.update_testrail(Environment.case_num, Environment.run_num , False, 'Test case failed')
    
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
