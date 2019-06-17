import os
import subprocess
import sys
import glob

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('./steps/'))
from base_setup import BaseSetup

sys.path.append(PATH('../generics/'))
import test_management

def start_execution(sys_port, feature_file=None, ports=None):
        
    if feature_file == None:
        subprocess.Popen(
            'behave -D APP_PATH=C:\\Users\\Administrator\\Downloads\\k3_app_170419.apk -D SYSPORT='+str(sys_port[i])+' -D UDID=' + str(device_list[i]) + ' -D DEVICE_TYPE=android -D MACHINE_TYPE=windows -D PORT=' + str(ports[i]) +' -D TESTRAIL_USER=archana.r@testyantra.com -D TESTRAIL_PASS=Pass1234',
            shell=False)
    else:
        subprocess.Popen(
            'behave -D APP_PATH=C:\\Users\\Administrator\\Downloads\\k3_app_170419.apk -D SYSPORT='+str(sys_port[i])+' -D UDID=' + str(device_list[i]) + ' -D DEVICE_TYPE=android -D MACHINE_TYPE=windows -D PORT=' + str(ports[i]) +' -D TESTRAIL_USER=archana.r@testyantra.com -D TESTRAIL_PASS=Pass1234 '+feature_file,
            shell=False)

try:    
    os.mkdir(PATH('..\\allure_reports\\'))
except:
    print "allure_reports directory present"
    
a_logs = glob.glob(PATH('../allure_reports/*'))
for f in a_logs:
    os.remove(f)

def start_execution2(feature_file,sys_port,ports=None):
    print feature_file[0]
    processes = None
    device_list=BaseSetup().get_list_of_devices()
    for i in range(len(device_list)):
        processes = subprocess.Popen(
                   'behave -D APP_PATH=C:\\Users\\Vinayaka\\Downloads\\k3_app.apk -D SYSPORT='+str(sys_port[i])+' -D UDID=' + str(device_list[i]) + ' -D DEVICE_TYPE=android -D MACHINE_TYPE=windows -D PORT=' + str(ports[i]) +' -D TESTRAIL_USER=archana.r@testyantra.com -D TESTRAIL_PASS=Pass1234 -f allure_behave.formatter:AllureFormatter -o ../allure_reports ' + feature_file[i], 
                   shell=False)


a=13000
tcp_port=[]
print type(tcp_port)
device_list=BaseSetup().get_list_of_devices()
for i in range(len(device_list)):
    tcp_port.append(a+i)

print tcp_port



b=4225
appium_port=[]
print type(tcp_port)
device_list=BaseSetup().get_list_of_devices()

for i in range(len(device_list)):
    appium_port.append(b+i*100)
print appium_port


feature_file=[]
print '----------'
print len(sys.argv)
print sys.argv[len(sys.argv)-1]
for i in range(1,len(sys.argv)):
    feature_file.append(sys.argv[i])
print feature_file


start_execution2(feature_file,tcp_port,appium_port)
