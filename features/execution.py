import subprocess
import os
import sys

sys.path.append('../generics/')
import test_management

def create_feature(suite_ID, project_ID, run_ID):
    test_management.create_feature_file(suite_ID, project_ID, run_ID)

def start_execution(feature_file=None):
    
    if feature_file == None:
        subprocess.Popen(
            'behave -D APP_PATH=C:\\Users\\Administrator.TNPLIND0007\\Downloads\\k123.apk -D DEVICE_TYPE=android -D MACHINE_TYPE=windows -D TESTRAIL_USER=archana.r@testyantra.com -D TESTRAIL_PASS=Pass1234',
            shell=False)
    else:
        subprocess.Popen(
            'behave -D APP_PATH=C:\\Users\\Administrator.TNPLIND0007\\Downloads\\k123.apk -D DEVICE_TYPE=android -D MACHINE_TYPE=windows -D TESTRAIL_USER=archana.r@testyantra.com -D TESTRAIL_PASS=Pass1234 '+feature_file,
            shell=False)


start_execution('MCQ_New_Choose.feature')