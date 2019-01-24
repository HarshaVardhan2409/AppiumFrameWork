from __builtin__ import str
from datetime import datetime
import os
import sys
import urllib2, json, base64

import constants
import generics_lib


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH(''))

#-----------------------------------------------------------------


class APIClient:
    def __init__(self, base_url):
        self.user = ''
        self.password = ''
        base_url = str(base_url)
        if not base_url.endswith('/'):
            base_url += '/'
        self.__url = base_url + 'index.php?/api/v2/'

    #
    # Send Get
    #
    # Issues a GET request (read) against the API and returns the result
    # (as Python dict).
    #
    # Arguments:
    #
    # uri                 The API method to call including parameters
    #                     (e.g. get_case/1)
    #
    def send_get(self, uri):
        return self.__send_request('GET', uri, None)

    #
    # Send POST
    #
    # Issues a POST request (write) against the API and returns the result
    # (as Python dict).
    #
    # Arguments:
    #
    # uri                 The API method to call including parameters
    #                     (e.g. add_case/1)
    # data                The data to submit as part of the request (as
    #                     Python dict, strings must be UTF-8 encoded)
    #
    def send_post(self, uri, data):
        return self.__send_request('POST', uri, data)

    def __send_request(self, method, uri, data):
        url = self.__url + uri
        request = urllib2.Request(url)
        if (method == 'POST'):
            request.add_data(json.dumps(data))
        auth = base64.b64encode('%s:%s' % (self.user, self.password))
        request.add_header('Authorization', 'Basic %s' % auth)
        request.add_header('Content-Type', 'application/json')

        e = None
        try:
            response = urllib2.urlopen(request).read()
        except urllib2.HTTPError as e:
            response = e.read()

        if response:
            result = json.loads(response)
        else:
            result = {}

        if e != None:
            if result and 'error' in result:
                error = '"' + result['error'] + '"'
            else:
                error = 'No additional error message received'
            raise APIError('TestRail API returned HTTP %s (%s)' % 
                (e.code, error))

        return result

class APIError(Exception):
    pass

#-------------------------------------------------------------------




testrail_file = constants.CONFIG_PATH
testrail_url = generics_lib.get_data(testrail_file, 'testrail', 'url')
testrail_username = 'archana.r@testyantra.com'
testrail_password = 'Pass1234'

def get_testrail_client():
    "Get the TestRail account credentials from the testrail.env file"
    #Get the TestRail Url
    client = APIClient(testrail_url)
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

def add_run(test_run_name, project_name, suite_id):
    client = get_testrail_client()
    project_id = get_project_id(project_name)
    try:
        result = client.send_post(
        'add_run/%s' %(project_id),
        {'suite_id': suite_id, 'name': test_run_name, 'include_all': True, })
        print result  
    except Exception, e:
        print 'Exception in add_run() updating TestRail.'
        print 'PYTHON SAYS: '
        print e
           
    return result        
def get_sections(project_ID, suite_ID): 
    client = get_testrail_client()
    # case = client.send_get('get_case/181')
    # print(case) 
    sections = client.send_get('get_sections/' + project_ID + '&suite_id=' + suite_ID)
    return sections

def get_section(section_ID): 
    client = get_testrail_client()
    # case = client.send_get('get_case/181')
    # print(case) 
    section = client.send_get('get_section/' + section_ID)
    return section
        
def create_feature_file(suite_ID, project_ID, run_ID): 
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
    
    f = None
    
    filedata = None
    section_id_1 = 0
    section_id_2 = 1
    count = 0
    
    for case in cases:
        if case['custom_autostatus'] != 3:
            
            section_id_1 = section_id_2
            section_id_2 = case['section_id']
            
            if section_id_1 != section_id_2:
                try:
                    f.write(filedata)
                    f.close()
                except:
                    print ''
                
                f = open(PATH('../features/' + feature_name + '_'  + str(get_section(str(section_id_2))['name']) + '.feature'), "w+")
                filedata = "@" + str(get_section(str(section_id_2))['name']) + '\nFeature: ' + str(get_section(str(section_id_2))['name']) + '\n'
                count += 1
                if case['custom_background'] != None:
                    filedata += ('\n\nBackground: ' + case['custom_background'].strip())
            if case['title'] != None:
                filedata += ('\n\n' + case['title'].strip() + ' testrail details_' + str(case['id']) + '_' + run_ID)     
            if case['custom_given'] != None:
                filedata += ('\nGiven ' + case['custom_given'].strip())
            if case['custom_when'] != None:
                filedata += ('\nWhen ' + case['custom_when'].strip())    
            if case['custom_then'] != None:
                filedata += ('\nThen ' + case['custom_then'].strip())
            if case['custom_example'] != None:
                filedata += ('\n\nExample ' + case['custom_example'].strip())
    f.write(filedata)
    f.close()
    print 'Number of feature file created = '+ str(count)

def create_feature_from_run(suite_ID, project_ID, run_ID): 
    client = APIClient(testrail_url)
    client.user = testrail_username
    client.password = testrail_password
    # case = client.send_get('get_case/181')
    # print(case) 
    suite = client.send_get('get_suite/' + suite_ID)
    feature_name = suite['name'].replace(" ", "_")
    # print suite
    cases = client.send_get('get_tests/' + run_ID)
    # print(cases[0])
    currenttime = datetime.now()
    curstr = currenttime.__str__().replace("-", "").replace(":", "").replace(" ", "")[0:12]
    
    f = None
    
    filedata = None
    section_id_1 = 0
    section_id_2 = 1
    count = 0
    
    for case in cases:
        if case['custom_autostatus'] != 3:
            
            section_id_1 = section_id_2
            section_id_2 = case['section_id']
            
            if section_id_1 != section_id_2:
                try:
                    f.write(filedata)
                    f.close()
                except:
                    print ''
                
                f = open(PATH('../features/' + feature_name + '_'  + str(get_section(str(section_id_2))['name']) + '.feature'), "w+")
                filedata = "@" + str(get_section(str(section_id_2))['name']) + '\nFeature: ' + str(get_section(str(section_id_2))['name']) + '\n'
                count += 1
                if case['custom_background'] != None:
                    filedata += ('\n\nBackground: ' + case['custom_background'].strip())
            if case['title'] != None:
                filedata += ('\n\n' + case['title'].strip() + ' testrail details_' + str(case['id']) + '_' + run_ID)     
            if case['custom_given'] != None:
                filedata += ('\nGiven ' + case['custom_given'].strip())
            if case['custom_when'] != None:
                filedata += ('\nWhen ' + case['custom_when'].strip())    
            if case['custom_then'] != None:
                filedata += ('\nThen ' + case['custom_then'].strip())
            if case['custom_example'] != None:
                filedata += ('\n\nExample ' + case['custom_example'].strip())
    f.write(filedata)
    f.close()
    print 'Number of feature file created = '+ str(count)

def create_feature_file_tags(suite_ID, project_ID, run_ID, tag_name=None): 
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
    
    f = None
    
    filedata = None
    section_id_1 = 0
    section_id_2 = 1
    count = 0
    
    tag_names = {"Installation": 1, "Onboarding": 2, "Android": 3, "IOS": 4, "Parity": 5, "Worksheets": 6, "World Map": 7, "Miscellaneous": 8, "Quest Progress": 9, "Chapters/Buildings": 10, "Quests": 11, "Tasks": 12, "Video": 13, "Game": 14, 
                 "Interactive Video": 15, "Interstitials": 16, "Sticker Book": 17, "Rewards": 18, "Online": 19, "Offline": 20, "Library": 21, "Parent Zone": 22, "Parent Gating": 23, "Profile Selection": 24, "Profile Picture": 25, "Child Report": 26, 
                 "OLAP/Analytics": 27, "Splash Screen": 28, "Transitions": 29, "FTUE": 30, "In-App Rating": 31, "Messaging": 32, "Payments": 33, "Subscription": 34, "Child Profile": 35, "Sessions": 36, "Device": 37, "Progress and Sync": 38, 
                 "Network": 39, "Security": 40, "MCQ": 41, "Classify": 42, "Sort": 43, "Hangman": 44, "Match": 45, "Choose": 46, "Count": 47}
    
    for case in cases:
        flag = False
        if tag_name == None:
            flag = True
        elif tag_names[tag_name] in case['custom_tags']:
            flag = True
        
        if case['custom_autostatus'] != 3 and flag:
            section_id_1 = section_id_2
            section_id_2 = case['section_id']
            
            if section_id_1 != section_id_2:
                try:
                    f.write(filedata)
                    f.close()
                except:
                    print ''
                
                f = open(PATH('../features/' + feature_name + '_'  + str(get_section(str(section_id_2))['name']) + '.feature'), "w+")
                filedata = "@" + str(get_section(str(section_id_2))['name']) + '\nFeature: ' + str(get_section(str(section_id_2))['name']) + '\n'
                count += 1
                if case['custom_background'] != None:
                    filedata += ('\n\nBackground: ' + case['custom_background'].strip())
            if case['title'] != None:
                filedata += ('\n\n' + case['title'].strip() + ' testrail details_' + str(case['id']) + '_' + run_ID)     
            if case['custom_given'] != None:
                filedata += ('\nGiven ' + case['custom_given'].strip())
            if case['custom_when'] != None:
                filedata += ('\nWhen ' + case['custom_when'].strip())    
            if case['custom_then'] != None:
                filedata += ('\nThen ' + case['custom_then'].strip())
            if case['custom_example'] != None:
                filedata += ('\n\nExample ' + case['custom_example'].strip())
    f.write(filedata)
    f.close()
    print 'Number of feature file created = '+ str(count)


def get_run(run_id):
    client = get_testrail_client()
    cases = client.send_get('get_case/' + run_id)
    print cases
    print type(cases)
    print '---------------------------------------------------------------------'
    '''
    for i in range(len(cases)):
        print cases[i]
        print '---------------------------------------------------------------------'
    '''
    
#get_run('4020')
#create_feature_file_tags('81', '2', '74')
#add_run('new_run_2', 'K3', '59')