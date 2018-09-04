from time import sleep

from ..Pages.classification import Classification
from ..generics import test_management

start_y = None
end_y = None

@given('User is main page of the classification application')
def user_is_main_page_of_the_application(context):
    context.classify = Classification(context.obj.altdriver, context.obj.driver)
    context.classify.verify_main_screen()


@when('User tap on Launch Classification button')
def user_tap_on_launch_classification_button(context):
    context.classify = Classification(context.obj.altdriver, context.obj.driver)
    context.classify.click_classification()

@then('Classification screen is loaded')
def classification_screen_is_loaded(context):
    context.classify = Classification(context.obj.altdriver, context.obj.driver)
    context.classify.verify_classification_screen()

@then('All the classification objects are loaded')
def all_the_objects_are_loaded(context):
    context.classify = Classification(context.obj.altdriver, context.obj.driver)
    context.classify.verify_classification_screen()
    sleep(3)

@given('Classification question 1 is loaded')
def question_1_is_loaded(context):
    context.classify = Classification(context.obj.altdriver, context.obj.driver)
    context.classify.verify_question_1('DraggableObject')

@when('User drag and drop the classification "{draggable}" to the bucket')
def user_drag_and_drop_the_draggables(context, draggable):
    context.classify = Classification(context.obj.altdriver, context.obj.driver)
    start_y = context.classify.object_location_y(draggable)
    context.classify.drag_object(draggable)
    sleep(2)

@then('Verify the classification "{draggable}"')
def verify_the_draggable(context, draggable):
    context.classify = Classification(context.obj.altdriver, context.obj.driver)
    end_y = context.classify.object_location_y(draggable)
    name = context.classify.object_name(draggable)
    if 'Stage_1' in name:
        if '1' in name or '2' in name:
            assert start_y != end_y
        if '3' in name or '4' in name or '5' in name:
            assert start_y != end_y
    elif 'Stage_2' in name:
        if '1' in name or '2' in name:
            assert start_y != end_y
        if '3' in name or '4' in name or '5' in name:
            assert start_y != end_y

@then('Update classification result to testrail "{caseID}"')
def update_result_to_testrail(context, caseID):
    if 'None' not in caseID:
        test_management.update_testrail(caseID, '11', True, 'Test case passed')

@given('Application is relaunched')
def application_is_relaunched(context):
    context
    
@given('Classification question 2 is loaded')
def question_2_is_loaded(context):
    context.classify = Classification(context.obj.altdriver, context.obj.driver)
    context.classify.verify_question_2('DraggableObject')
