import os
import subprocess
import sys

from altunityrunner import AltrunUnityDriver
from appium import webdriver
from selenium.webdriver.common.by import By




PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../games/templates/'))
from base_class import BaseClass
sys.path.append(PATH('../../generics/'))
import constants
import generics_lib

class BaseSetup():
    
    altdriver = None
    driver = None
    platform = None  # set to `ios` or `android` to change platform
    system_os = None
    app_path = None
    desired_caps = None
    ip_address = None
    sys_port = None
    port = None
    udid = None
    version=None
    def install_app(self):
        print '---------udid and port---------------------------'
        print self.udid
        print self.port
        print '------------------------------------'
        self.desired_caps = {}
        if ("android" in self.platform.lower()):
            self.setup_android(False)
        elif ("ios" in self.platform.lower()):
            self.setup_ios(False)
        else:
            print 'platform do not match'
            
        self.ip_address = generics_lib.get_data(constants.CONFIG_PATH, 'appium_server', 'ip_address')
        self.driver = webdriver.Remote('http://'+self.ip_address+':'+self.port+'/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(20)
        print "================================="
        print self.port+ "launched "
        print "================================="
        
        self.altdriver = AltrunUnityDriver(self.driver, self.platform,TCP_FWD_PORT=int(self.sys_port),deviceID=self.udid,requestEnd='#')
        

        
    def teardown(self):
        self.altdriver.stop()
        self.driver.quit()
        
    def setup_android(self ,flag):
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['deviceName'] = 'device'
        self.desired_caps['udid'] = self.udid
        self.desired_caps['noReset'] = flag
        self.desired_caps['app'] = self.app_path
        self.desired_caps['newCommandTimeout'] = 300

    # This will be handled with iOS implementation.
    def setup_ios(self,flag):
        self.desired_caps['platformName'] = 'iOS'
        self.desired_caps['deviceName'] = 'device'
        self.desired_caps['udid'] = self.udid
        self.desired_caps['automationName'] = 'XCUITest'
        self.desired_caps['app'] = self.app_path
        self.desired_caps['newCommandTimeout'] = 300
        
    def launch_app(self):

        print '---------udid and port---------------------------'
        print self.udid
        print self.port
        print '------------------------------------'
        self.desired_caps = {}
        if ("android" in self.platform.lower()):
            self.setup_android(True)
        elif ("ios" in self.platform.lower()):
            self.setup_ios(True)
        else:
            print 'platform do not match'
          
        self.ip_address = generics_lib.get_data(constants.CONFIG_PATH, 'appium_server', 'ip_address')
        self.driver = webdriver.Remote('http://'+self.ip_address+':'+self.port+'/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(20)
        self.altdriver = AltrunUnityDriver(self.driver, self.platform,TCP_FWD_PORT=int(self.sys_port),deviceID=self.udid,requestEnd='#')
               
   
        
    def get_list_of_devices(self):  
        device_list=[]
        tee=subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE)
        stdout = tee.communicate()[0]
        sttt=str('STDOUT:{}'.format(stdout))
        nam=sttt.split()
        val= len(sttt.split())
        for i in range(val):
            if(nam[i]=='device'):
                device_list.append(nam[i-1])  
                
        return device_list
    
    def getting_logs(self):
        self.base_class = BaseClass(self.altdriver, self.driver)
        self.base_class.demo()
        
    def togetLogs(self):
        print "Type of driver"
        print type(self.driver)
        print self.driver.log_types