from testrail import *
import time
import test_management

client = APIClient(test_management.testrail_url)
client.user = test_management.testrail_user
client.password = test_management.testrail_password

def get_comparision_report(num, num2):
    run = client.send_get('get_run/' + num)
    run2 = client.send_get('get_run/' + num2)
    f = open("compreport" + '.html', "wb")
    data = "<html><head><style>"
    data += "table, th, td { \n border: 1px solid black;"
    data += "border-collapse: collapse;}"
    data += "th, td {padding: 15px;text-align: left;}"
    data += "table{ width: 40%;background-color:#ffb3b3;}"
    data += "</style></head><body bgcolor='#ffffcc'>"
    data += "<center><h2><font color='purple'>Comparision Report</h2></center>"
    data += "<table ><col width='30'><col width='30'><col width='30'><tr>"
    f.write(data)
    f = open("compreport" + '.html', "ab")
    filedata = ("<tr><td>" + "Name " + "</td><td>" + run['name'] + "</td><td>" + run2['name'] + "</td></tr>")
    filedata += (" <tr><td>" + "Passed_Count" + "</td><td>" + str(run['passed_count'],) + "</td><td>" + str(run2['passed_count'],) + "</td></tr>")
    filedata += (" <tr><td>" + "Failed_Count" + "</td><td>" + str(run['failed_count']) + "</td><td>" + str(run2['failed_count']) + "</td></tr>")
    filedata += (" <tr><td>" + "Blocked_Count" + "</td><td>" + str(run['blocked_count']) + "</td><td>" + str(run2['blocked_count']) + "</td></tr>")
    filedata += (" <tr><td>" + "Retest_Count" + "</td><td>" + str(run['retest_count']) + "</td><td>" + str(run2['retest_count']) + "</td></tr>")
    filedata += (" <tr><td>" + "Untested_Count" + "</td><td>" + str(run['untested_count']) + "</td><td>" + str(run2['untested_count']) + "</td></tr>")
    filedata += (" <tr><td>" + "Created_On" + "</td><td>" + time.ctime(run['created_on']) + "</td><td>" + time.ctime(run2['created_on']) + "</td></tr>")
    f.write(filedata)
    f = open("compreport" + '.html', "ab")
    data = "</tr></table></body></html>"
    f.write(data)
    f.close()