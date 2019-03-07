'''
This module contains generic methods which are mobile specific
'''

import json
import sys

from matplotlib.pyplot import imread
from scipy.linalg import norm
from scipy import sum, average
from skimage.measure import compare_ssim

from selenium.webdriver.common.action_chains import ActionChains

    
def scroll(driver, start_xvalue, end_xvalue, start_yvalue, end_yvalue, duration=0):
    dSize = (driver.get_window_size())
    start_x = (dSize['width']*start_xvalue)
    end_x = (dSize['width']*end_xvalue)
    start_y = (dSize['height']*start_yvalue)
    end_y = (dSize['height']*end_yvalue)
    driver.swipe(start_x, start_y, end_x, end_y, duration)
    
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
    
def takescreenshot(driver, path):
    driver.save_screenshot(path)
    
def compare_images(image_1, image_2):
    file1 = image_1
    file2 = image_2

    # read images as 2D arrays (convert to grayscale for simplicity)
    img1 = to_grayscale(imread(file1).astype(float))
    img2 = to_grayscale(imread(file2).astype(float))
    # compare
    n_m, n_0 = compare(img1, img2)
    print "1st norm:", n_m, "/ per pixel:", n_m/img1.size
    print "2nd norm:", n_0, "/ per pixel:", n_0*1.0/img1.size
    if n_m != 0.0:
        percentage = n_m/n_0
        print str(int(percentage)) + '%'
        return int(percentage)
    else:
        print '0%'
        return 0
    
def compare(img1, img2):
    # normalize to compensate for exposure difference, this may be unnecessary
    # consider disabling it
    img1 = normalize(img1)
    img2 = normalize(img2)
    # calculate the difference and its norms
    diff = img1 - img2  # elementwise for scipy arrays
    m_norm = sum(abs(diff))  # Manhattan norm
    z_norm = norm(diff.ravel(), 0)  # Zero norm
    return (m_norm, z_norm)

def to_grayscale(arr):
    "If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr
    
def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng

def compare_video_images(file1, file2):
    img_a = to_grayscale(imread(file1).astype(float))
    img_b = to_grayscale(imread(file2).astype(float))
    
    img_1 = normalize(img_a)
    img_2 = normalize(img_b)
    # score: {-1:1} measure of the structural similarity between the images
    score, diff = compare_ssim(img_1, img_2, full=True)
    score = int(score * 100)
    print(score)
    return score

#compare_video_images("C:\\Users\\Vinayaka\\Downloads\\correct1.png", "C:\\Users\\Vinayaka\\Downloads\\correct1.png")