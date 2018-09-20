'''
This module contains generic methods
'''

import json

from selenium.webdriver.common.action_chains import ActionChains

    
def scroll(driver, start_xvalue, end_xvalue, start_yvalue, end_yvalue):
    dSize = (driver.get_window_size())
    start_x = (dSize['width']*start_xvalue)
    end_x = (dSize['width']*end_xvalue)
    start_y = (dSize['height']*start_yvalue)
    end_y = (dSize['height']*end_yvalue)
    driver.swipe(start_x, start_y, end_x, end_y)
    
def action_sendkeys(driver, text):
        action = ActionChains(driver);
        action.send_keys(text).perform()
        
def get_data(file, group_name, key):
        with open(file) as f:
            data = json.load(f)
            value = data[group_name][key]
        return value
    
def action_sendkeys_to_elements(driver, text):
    driver.find_element_by_xpath('//android.widget.EditText[@index="0"]').send_keys(text)