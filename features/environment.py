from __builtin__ import str
import os
import shutil
import subprocess
import sys
from time import sleep

from steps.base_setup import BaseSetup
sys.path.append('../generics/')
import test_management
import constants
import generics_lib
        
obj = BaseSetup()

def before_all(context):
    BaseSetup.app_path = str(context.config.userdata['APP_PATH'])
    device_type = str(context.config.userdata['DEVICE_TYPE']).lower()
    machine_type = str(context.config.userdata['MACHINE_TYPE']).lower()
    BaseSetup.platform = device_type
    BaseSetup.system_os = machine_type
    
    test_management.testrail_username = str(context.config.userdata['TESTRAIL_USER'])
    test_management.testrail_password = str(context.config.userdata['TESTRAIL_PASS'])
    
    '''
    To clear the prvious execution data
    ''' 
    shutil.rmtree(constants.PATH('../execution_data/app_logs/'))
    os.mkdir(constants.PATH('../execution_data/app_logs/'))
    shutil.rmtree(constants.PATH('../execution_data/reports/'))
    os.mkdir(constants.PATH('../execution_data/reports/'))
    shutil.rmtree(constants.PATH('../execution_data/screenshots/'))
    os.mkdir(constants.PATH('../execution_data/screenshots/'))
    
    if 'android' in device_type:
        subprocess.Popen('adb forward tcp:13001 tcp:13000', shell=True)
    elif 'ios' in device_type:
        subprocess.Popen('iproxy forward tcp:13001 tcp:13000', shell=True)
    subprocess.Popen('appium', shell=True)
    sleep(40)
    context.obj = obj
    context.obj.setup()
    
def before_feature(context, feature):
    device_type = str(context.config.userdata['DEVICE_TYPE']).lower()
    if 'android' in device_type:
        subprocess.Popen('adb logcat -c', shell=True)
        package_name = generics_lib.get_data(constants.config_path, 'app_config', 'logs')
        subprocess.Popen('adb logcat | findstr ' + package_name + ' > ' + constants.PATH('../execution_data/app_logs/logs_' + feature.name + '.txt'), shell=True)

def before_scenario(context, scenario):
    data = None
    data = str(context.scenario)
    data = data.split('">')
    data = data[0].split('_')
    data.reverse()
    device_type = str(context.config.userdata['DEVICE_TYPE']).lower()
    '''
    if 'android' in device_type:
        subprocess.Popen('adb logcat -c', shell=True)
        package_name = generics_lib.get_data(constants.config_path, 'app_config', 'logs')
        subprocess.Popen('adb logcat | findstr ' + package_name + ' > ' + constants.PATH('../execution_data/app_logs/logs_caseID_' + data[1] + '_runID_' + data[0] + '.txt'), shell=True)
    '''

def after_scenario(context, scenario):
    
    machine_type = str(context.config.userdata['MACHINE_TYPE']).lower()
    BaseSetup.system_os = machine_type
    
    context.obj = obj
    
    data = None
    data = str(context.scenario)
    data = data.split('">')
    data = data[0].split('_')
    data.reverse()
    
    if context.failed:
        directory = constants.PATH('../execution_data/screenshots/failed_caseID_' + data[1] + '_runID_' + data[0] + '.png')
        context.obj.driver.save_screenshot(directory)
        
        test_management.update_testrail(data[1], data[0] , False, 'Test case failed')
    else:
        test_management.update_testrail(data[1], data[0] , True, 'Test case passed')
    context.obj.relaunch_app()

def after_all(context):
    
    context.obj = obj
    context.obj.teardown()
    
    machine_type = str(context.config.userdata['MACHINE_TYPE']).lower()
    
    if 'windows' in machine_type:
        # Use below code to Stop appium server on the local windows machine
        subprocess.Popen('Taskkill /IM adb.exe /F',shell=True)
        subprocess.Popen('Taskkill /IM node.exe /F',shell=True)
        
    else:
        # Use below code to stop appium server on the local mac machine
        subprocess.Popen('killall node',shell=True)

