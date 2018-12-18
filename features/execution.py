import subprocess
import os
import sys

import sys
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def start_execution(feature_file=None):
        
    if feature_file == None:
        subprocess.Popen(
            'behave -D APP_PATH=C:\\Users\\Administrator.TNPLIND0007\\Downloads\\k123_app.apk -D DEVICE_TYPE=android -D MACHINE_TYPE=windows -D TESTRAIL_USER=archana.r@testyantra.com -D TESTRAIL_PASS=Pass1234',
            shell=False)
    else:
        subprocess.Popen(
            'behave -D APP_PATH=C:\\Users\\Administrator.TNPLIND0007\\Downloads\\k123_app.apk -D DEVICE_TYPE=android -D MACHINE_TYPE=windows -D TESTRAIL_USER=archana.r@testyantra.com -D TESTRAIL_PASS=Pass1234 '+feature_file,
            shell=False)
# -f allure_behave.formatter:AllureFormatter -o ../execution_data/reports 


start_execution(str(sys.argv[1]))
