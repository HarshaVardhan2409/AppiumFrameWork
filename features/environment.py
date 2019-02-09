from __builtin__ import str
import os
import shutil
import subprocess
import sys
from time import sleep
from behave.model_core import Status

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
sys.path.append(PATH('./games/templates/'))
from base_class import BaseClass

sys.path.append(PATH('./steps/'))
from base_setup import BaseSetup

sys.path.append(PATH('../generics/'))
import constants
import generics_lib
import test_management

obj = BaseSetup()

def before_all(context):
    BaseSetup.app_path = str(context.config.userdata['APP_PATH'])
    device_type = str(context.config.userdata['DEVICE_TYPE']).lower()
    machine_type = str(context.config.userdata['MACHINE_TYPE']).lower()
    BaseSetup.platform = device_type
    BaseSetup.system_os = machine_type
    BaseClass.platform = device_type
    
    test_management.testrail_username = str(context.config.userdata['TESTRAIL_USER'])
    test_management.testrail_password = str(context.config.userdata['TESTRAIL_PASS'])
    
    '''
    to create the execution directory and other sub directories
    '''
    try:    
        os.mkdir(constants.PATH('..\\execution_data\\'))
        os.mkdir(constants.PATH('..\\execution_data\\app_logs\\'))
        os.mkdir(constants.PATH('..\\execution_data\\reports\\'))
        os.mkdir(constants.PATH('..\\execution_data\\screenshots\\'))
        os.mkdir(constants.PATH('..\\compare_images\\'))
    except:
        print "execution directory present"
    
    '''
    To clear the previous execution data
    ''' 
    shutil.rmtree(constants.PATH('../execution_data/app_logs/'))
    os.mkdir(constants.PATH('../execution_data/app_logs/'))
    shutil.rmtree(constants.PATH('../execution_data/reports/'))
    os.mkdir(constants.PATH('../execution_data/reports/'))
    shutil.rmtree(constants.PATH('../execution_data/screenshots/'))
    os.mkdir(constants.PATH('../execution_data/screenshots/'))
    shutil.rmtree(constants.PATH('../compare_images/'))
    os.mkdir(constants.PATH('../compare_images/'))
    
    '''
    port forwarding for android and ios
    '''
    if 'android' in device_type:
        subprocess.Popen('adb forward tcp:13000 tcp:13000', shell=True)
    elif 'ios' in device_type:
        subprocess.Popen('iproxy forward tcp:13000 tcp:13000', shell=True)
        
    '''
    starting appium server
    '''
    subprocess.Popen('appium', shell=True)
    sleep(40)
    context.obj = obj
    
def before_feature(context, feature):
    device_type = str(context.config.userdata['DEVICE_TYPE']).lower()
    machine_type = str(context.config.userdata['MACHINE_TYPE']).lower()
    
    '''
    capturing the logs for every feature files
    '''
    if 'android' in device_type:
        subprocess.Popen('adb logcat -c', shell=True)
        package_name = generics_lib.get_data(constants.CONFIG_PATH, 'app_config', 'logs')
        if 'windows' in machine_type:
            subprocess.Popen('adb logcat | findstr ' + package_name + ' > ' + constants.PATH('../execution_data/app_logs/logs_' + feature.name + '.txt'), shell=True)
        else:
            subprocess.Popen('adb logcat | grep ' + package_name + ' > ' + constants.PATH('../execution_data/app_logs/logs_' + feature.name + '.txt'), shell=True)

def before_scenario(context, scenario):
    data = None
    data = str(context.scenario)
    data = data.split('">')
    data = data[0].split('_')
    data.reverse()
    device_type = str(context.config.userdata['DEVICE_TYPE']).lower()
    machine_type = str(context.config.userdata['MACHINE_TYPE']).lower()
    
    '''
    capturing the logs for every scenario files
    '''
    if 'android' in device_type:
        subprocess.Popen('adb logcat -c', shell=True)
        package_name = generics_lib.get_data(constants.CONFIG_PATH, 'app_config', 'logs')
        if 'windows' in machine_type:
            subprocess.Popen('adb logcat | findstr ' + package_name + ' > ' + constants.PATH('../execution_data/app_logs/logs_caseID_' + data[1] + '_runID_' + data[0] + '.txt'), shell=True)

def after_scenario(context, scenario):
    
    machine_type = str(context.config.userdata['DEVICE_TYPE']).lower()
    BaseSetup.platform = machine_type
    
    #context.obj = obj
    
    '''
    updating result to testrail
    '''
    
    data = None
    data = str(context.scenario)
    data = data.split('">')
    data = data[0].split('_')
    data.reverse()
    try:
            
        if scenario.status == Status.failed:
            
            directory = constants.PATH('../execution_data/screenshots/failed_caseID_' + data[1] + '_runID_' + data[0] + '.png')
            context.obj.driver.save_screenshot(directory)
            
            test_management.update_testrail(data[1], data[0] , False, 'Test case failed')
            
        elif scenario.status == Status.skipped:
            test_management.update_testrail(data[1], data[0] , False, 'Test case skipped')
            
        elif scenario.status == Status.untested:
            test_management.update_testrail(data[1], data[0] , False, 'Test case untested')
            
        else:
            test_management.update_testrail(data[1], data[0] , True, 'Test case passed')
            
    except:
        print 'Test case ID or the Test Run ID does not match'
    

def after_all(context):
    context.obj = obj
    
    machine_type = str(context.config.userdata['MACHINE_TYPE']).lower()
    '''
    closing the appium server
    '''
    if 'windows' in machine_type:
        # Use below code to Stop appium server on the local windows machine
        subprocess.Popen('Taskkill /IM adb.exe /F',shell=True)
        subprocess.Popen('Taskkill /IM node.exe /F',shell=True)
        
    else:
        # Use below code to stop appium server on the local mac machine
        subprocess.Popen('killall node',shell=True)
