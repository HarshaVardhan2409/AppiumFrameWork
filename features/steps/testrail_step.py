import sys

sys.path.append('.../generics/')
import test_management

@then('Update result to testrail')
def update_result_to_testrail(context):
    for row in context.table:
        test_management.update_testrail(row["caseID"], row["suiteID"], True, 'Test case passed')
        