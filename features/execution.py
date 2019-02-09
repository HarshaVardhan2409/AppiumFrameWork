import subprocess
import os
import sys


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../generics/'))
import test_management

def create_feature(suite_ID, project_ID, run_ID):
    test_management.create_feature_file(suite_ID, project_ID, run_ID)

def start_execution(feature_file=None):
        
    if feature_file == None:
        subprocess.Popen(
            'behave -D APP_PATH=C:\\Users\\Vinayaka\\Downloads\\k3_app.apk -D DEVICE_TYPE=android -D MACHINE_TYPE=windows -D TESTRAIL_USER=archana.r@testyantra.com -D TESTRAIL_PASS=Pass1234',
            shell=False)
    else:
        subprocess.Popen(
            'behave -D APP_PATH=C:\\Users\\Vinayaka\\Downloads\\k3_app.apk -D DEVICE_TYPE=android -D MACHINE_TYPE=windows -D TESTRAIL_USER=archana.r@testyantra.com -D TESTRAIL_PASS=Pass1234 '+feature_file,
            shell=False)
        
        
        
# -f allure_behave.formatter:AllureFormatter -o ../execution_data/reports sys.argv[4]--processes 2 --parallel-element scenario 


suite_id = str(sys.argv[1]).split(',')
suite_len = len(suite_id)
run_id = str(sys.argv[3]).split(',')
run_len = len(run_id)
if suite_len == run_len:
    for i in range(suite_len):
        create_feature(suite_id[i], str(sys.argv[2]), run_id[i])
else:
    print 'Invalid number of suites or runs'

#start_execution('Hangman_New_g3eq96-mcq1.feature')
#create_feature(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))
#start_execution('--tags=@smoke mcq_batch1_G3MQ39.feature')
#start_execution('-f allure_behave.formatter:AllureFormatter -o ../execution_data/reports Account_creation.feature InstallationOnboarding.feature Library.feature chapterandquestflow.feature parentzone.feature')


