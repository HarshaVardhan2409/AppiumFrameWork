from ..generics import test_management


@then('Update mcq result to testrail "{caseID}"')
def update_result_to_testrail(context, caseID):
    if 'None' not in caseID:
        test_management.update_testrail(caseID, '15', True, 'Test case passed')