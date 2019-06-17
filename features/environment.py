import os
import shutil
import subprocess
import glob
import sys
from time import sleep
from behave.model_core import Status
import ipdb
import traceback

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

BEHAVE_DEBUG_ON_ERROR = True

def before_all(context):
    BaseSetup.app_path = str(context.config.userdata['APP_PATH'])
    BaseSetup.udid = str(context.config.userdata['UDID'])
    BaseSetup.port = str(context.config.userdata['PORT'])
    BaseSetup.sys_port=str(context.config.userdata['SYSPORT'])
    device_type = str(context.config.userdata['DEVICE_TYPE']).lower()
    machine_type = str(context.config.userdata['MACHINE_TYPE']).lower()
    BaseSetup.platform = device_type
    BaseSetup.system_os = machine_type
    BaseClass.platform = device_type
    '''
    closing the appium server
    '''
    if 'windows' in machine_type:
        # Use below code to Stop appium server on the local windows machine
        subprocess.Popen('adb -s'+ BaseSetup.udid +' shell input keyevent KEYCODE_WAKEUP', shell=True, stdout=subprocess.PIPE)
        subprocess.Popen('Taskkill /IM adb.exe /F',shell=True)
        subprocess.Popen('Taskkill /IM node.exe /F',shell=True)
        print ''
         
    else:
        # Use below code to stop appium server on the local mac machine
        subprocess.Popen('killall node',shell=True)
    print "==================port value======"
    print BaseSetup.port
    print "===============port value========="
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
    a_logs = glob.glob(constants.PATH('../execution_data/app_logs/*'))
    for f in a_logs:
        os.remove(f)
    rep = glob.glob(constants.PATH('../execution_data/reports/*'))
    for f in rep:
        os.remove(f)
    scr = glob.glob(constants.PATH('../execution_data/screenshots/*'))
    for f in scr:
        os.remove(f)
    c_image = glob.glob(constants.PATH('../compare_images/*'))
    for f in c_image:
        os.remove(f)
    
    '''
    port forwarding for android and ios
    Handled while creating AltrunUnityDriver
    '''
    sleep(10)
    print "starting server"
    '''
    starting appium server
    '''
    subprocess.Popen('appium -p'+BaseSetup.port+' -bp '+str(int(BaseSetup.port)+1000)+' --relaxed-security', shell=True)
    sleep(10)
    context.obj = obj
    
def before_feature(context, feature):
    device_type = str(context.config.userdata['DEVICE_TYPE']).lower()
    machine_type = str(context.config.userdata['MACHINE_TYPE']).lower()
    dirname = os.path.dirname(__file__)
    print "entering before feature"
    print dirname
    print feature.name
    #filename=constants.PATH(feature.name+'.feature')
    filename = os.path.join(dirname,feature.name+'.feature')
    f = open(filename,'r')
    for line in f:
        if '@B' not in line:
            vers=line
            break
    f.close()
    BaseSetup.version =vers
    print BaseSetup.version
    '''
    capturing the logs for every feature files
    '''
    if 'android' in device_type:
        subprocess.Popen('adb -s'+BaseSetup.udid+'logcat -c', shell=True)
        package_name = generics_lib.get_data(constants.CONFIG_PATH, 'app_config', 'logs')
        if 'windows' in machine_type:
            subprocess.Popen('adb -s'+BaseSetup.udid+'logcat | findstr ' + package_name + ' > ' + constants.PATH('../execution_data/app_logs/logs_' + feature.name + '.txt'), shell=True)
        else:
            subprocess.Popen('adb -s'+BaseSetup.udid+' logcat | grep ' + package_name + ' > ' + constants.PATH('../execution_data/app_logs/logs_' + feature.name + '.txt'), shell=True)
    
def before_scenario(context, scenario):
    data = None
    data = str(context.scenario)
    data = data.split('">')
    data = data[0].split('_')
    data.reverse()
    device_type = str(context.config.userdata['DEVICE_TYPE']).lower()
    machine_type = str(context.config.userdata['MACHINE_TYPE']).lower()
    
def after_step(context, step):
    try:
        print "===================="
    except:
        print '......................'
            
def after_scenario(context, scenario):
    
    machine_type = str(context.config.userdata['DEVICE_TYPE']).lower()
    BaseSetup.platform = machine_type
    '''
    updating result to testrail
    '''
    data = None
    failed_details = ''
    error_msg = ''
    exception = ''
    step_name = ''
    headings = ''
    row = ''
    data = str(context.scenario)
    print "========================data after scenario"

    print data
    data = data.split('">')
    data = data[0].split('_')
    data.reverse()
    print scenario.steps
    for step in scenario.steps:
        if step.status == Status.failed and BEHAVE_DEBUG_ON_ERROR:
            '''capturing assertion error message'''
            try:
                error_msg = str(step.error_message)
            except:
                error_msg = 'No error message available'
                
            '''capturing excepting'''
            try:
                tb = traceback.extract_tb(step.exc_traceback)
                for val1 in tb:
                    for i in range(len(val1)):
                        if i==0:
                            exception = exception +'File "'+str(val1[i])+'"; '
                        elif i==1:
                            exception = exception + 'at line '+str(val1[i])+', '
                        elif i==2:
                            exception = exception + 'in '+str(val1[i])+'\n'
                        elif i==3:
                            exception = exception + str(val1[i])+'\n'
            except:
                exception = 'No exception available'
                
            '''capturing step name'''
            try:
                step_name = str(step.keyword)+' '+step.name
            except:
                step_name = 'No step available'
            '''capturing step table'''    
            try:
                print 'headings list ================='
                print step.table.headings
                print type(step.table.headings)
                for head in step.table.headings:
                    print 'printing head==============='
                    print head
                    headings = headings +'| ' + head
                headings = headings + '|'
                print headings
                print 'rows list ================='
                print step.table.rows[0].cells
                print type(step.table.rows[0].cells)
                for m in step.table.rows:
                    for n in m.cells:
                        print 'printing i=========='
                        row = row +'| ' + str(n)
                row = row + '|'
                print 'row'
                
            except:
                headings = 'No step table'
                row = ''
            try:
                failed_details = error_msg + '\nException:\n' + exception + '\nStep:\n' + step_name + '\n' + headings +' \n' + row
            except Exception as e:
                print str(e)
                failed_details = str(e)
    print failed_details
    try:
        if scenario.status == Status.failed:
            directory = constants.PATH('../execution_data/screenshots/failed_caseID_' + data[1] + '_runID_' + data[0] + '.png')
            context.obj.driver.save_screenshot(directory)
           
            test_management.update_testrail(data[1], data[0] , False, failed_details)
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
    subprocess.Popen('adb -s'+ BaseSetup.udid +' shell input keyevent KEYCODE_POWER', shell=True, stdout=subprocess.PIPE)
    '''
    closing the appium server
    '''
#     if 'windows' in machine_type:
# #         Use below code to Stop appium server on the local windows machine
#         subprocess.Popen('Taskkill /IM adb.exe /F',shell=True)
#         subprocess.Popen('Taskkill /IM node.exe /F',shell=True)
#         print ''
#         
#     else:
#         # Use below code to stop appium server on the local mac machine
#         subprocess.Popen('killall node',shell=True)
