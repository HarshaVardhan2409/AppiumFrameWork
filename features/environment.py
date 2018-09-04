from __builtin__ import str
import subprocess
from time import sleep

from steps.base_setup import Base_Setup
import sys

sys.path.append('../generics/')
import test_management

obj = Base_Setup()

def before_all(context):
    Base_Setup.app_path = str(context.config.userdata['APP_PATH'])
    device_type = str(context.config.userdata['DEVICE_TYPE'])
    
    test_management.testrail_username = str(context.config.userdata['TESTRAIL_USER'])
    test_management.testrail_password = str(context.config.userdata['TESTRAIL_PASS'])
    if 'android' in device_type:
        subprocess.Popen('adb forward tcp:13001 tcp:13000', shell=True)
    elif 'ios' in device_type:
        subprocess.Popen('iproxy forward tcp:13001 tcp:13000', shell=True)
    subprocess.Popen('appium', shell=True)
    sleep(15)
    
def before_feature(context, feature):
    value = str(feature)
    context.obj = obj
    context.obj.setup()
    
def before_step(context, step):
    context.obj = obj
    if 'Application is relaunched' in step.name:
        try:
            sleep(2)
            context.obj.teardown()
            sleep(2)
            context.obj.setup()
        except:
            print 'Error in relaunch'
    
def after_feature(context, feature):
    value = str(feature)
    context.obj = obj
    context.obj.teardown()
    
def after_all(context):
    # Use below code to Stop appium server on the local windows machine
    #call(["cmd.exe",'/c',"Taskkill /IM node.exe /F"])

    # Use below code to stop appium server on the local mac machine
    subprocess.Popen('killall node',shell=True)