'''
This module contains generic methods
'''
import os
import json
import dotenv
from selenium.webdriver.common.action_chains import ActionChains

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Generics():
    
    def scroll(self, driver, start_xvalue, end_xvalue, start_yvalue, end_yvalue):
        dSize = (driver.get_window_size())
        start_x = (dSize['width']*start_xvalue)
        end_x = (dSize['width']*end_xvalue)
        start_y = (dSize['height']*start_yvalue)
        end_y = (dSize['height']*end_yvalue)
        driver.swipe(start_x, start_y, end_x, end_y)
        
    def get_data(self, file, group_name, key):
        with open(file) as f:
            data = json.load(f)
            value = data[group_name][key]
        return value
    
def get_value(conf, key):
        "Return the value in conf for a given key"
        value = None
        try:
            dotenv.load_dotenv(conf)
            value = os.environ[key]
        except Exception, e:
            print 'Exception in get_value'
            print 'file: ', conf
            print 'key: ', key
        return value
    
def action_sendkeys(driver, text):
        action = ActionChains(driver);
        action.send_keys(text).perform()
        
def get_data(file, group_name, key):
        with open(file) as f:
            data = json.load(f)
            value = data[group_name][key]
        return value