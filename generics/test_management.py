from datetime import datetime

from testrail import *
import testrail

import generics_lib
import constants

testrail_file = constants.config_path
testrail_url = generics_lib.get_data(testrail_file, 'testrail', 'url')
testrail_username = None
testrail_password = None

def get_testrail_client():
    "Get the TestRail account credentials from the testrail.env file"
    #Get the TestRail Url
    client = testrail.APIClient(testrail_url)
    #Get and set the TestRail User and Password
    client.user = testrail_username
    client.password = testrail_password
    return client

def update_testrail(case_id, run_id, result_flag, msg=""):
    "Update TestRail for a given run_id and case_id"
    update_flag = False
    #Get the TestRail client account details
    client = get_testrail_client()
 
    #Update the result in TestRail using send_post function. 
    #Parameters for add_result_for_case is the combination of runid and case id. 
    #status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed
    status_id = 1 if result_flag is True else 5
 
    if run_id is not None:
        try:
            result = client.send_post(
                'add_result_for_case/%s/%s'%(run_id, case_id),
                {'status_id': status_id, 'comment': msg })
        except Exception, e:
            print 'Exception in update_testrail() updating TestRail.'
            print 'PYTHON SAYS: '
            print e
        else:
            print 'Updated test result for case: %s in test run: %s with msg:%s' % (case_id, run_id, msg)
 
    return update_flag

def get_project_id(project_name):
        "Get the project ID using project name"
        client = get_testrail_client()
        project_id = None
        projects = client.send_get('get_projects')
        for project in projects:
            if project['name'] == project_name: 
                project_id = project['id']
                #project_found_flag=True
                break
        print project_id
        return project_id
 
def get_run_id(test_run_name, project_name):
        "Get the run ID using test name and project name"
        run_id = None
        client = get_testrail_client()
        project_id = get_project_id(project_name)
        try:
            test_runs = client.send_get('get_runs/%s' % (project_id))
        except Exception, e:
            print 'Exception in update_testrail() updating TestRail.'
            print 'PYTHON SAYS: '
            print e
            return None
        else:
            for test_run in test_runs:
                if test_run['name'] == test_run_name:
                    run_id = test_run['id']
                    break
            return run_id
        
def create_feature_file(suite_ID, project_ID): 
    client = APIClient(testrail_url)
    client.user = testrail_username
    client.password = testrail_password
    # case = client.send_get('get_case/181')
    # print(case) 
    suite = client.send_get('get_suite/' + suite_ID)
    feature_name = suite['name'].replace(" ", "_")
    # print suite
    cases = client.send_get('get_cases/' + project_ID + '&suite_id=' + suite_ID)
    # print(cases[0])
    currenttime = datetime.now()
    curstr = currenttime.__str__().replace("-", "").replace(":", "").replace(" ", "")[0:12]
    
    f = open('../' + feature_name + '.feature', "w+")
    filedata = "@" + feature_name + '\nFeature: ' + feature_name + '\n'
    
    for case in cases:
        if case['custom_background'] != None:
            filedata += ('\n\n\tBackground: ' + case['custom_background'].strip())
        if case['title'] != None:
            filedata += ('\n\t\t' + case['title'].strip())     
        if case['custom_given'] != None:
            filedata += ('\n\t\t\tGiven ' + case['custom_given'].strip())
        if case['custom_when'] != None:
            filedata += ('\n\t\t\tWhen ' + case['custom_when'].replace("And", '\n\t\t\tAnd').strip())    
        if case['custom_then'] != None:
            filedata += ('\n\t\t\tThen ' + case['custom_then'].strip())
        if case['custom_example'] != None:
            filedata += ('\n\n\t\tExample ' + case['custom_example'].strip())
    f.write(filedata)
    f.close()
    