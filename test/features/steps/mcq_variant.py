from time import sleep

from ..Pages.mcq import MCQ

start_y = None
end_y = None

@given('User is main page of the mcq application')
def user_is_main_page_of_the_application(context):
    context.mcq = MCQ(context.obj.altdriver, context.obj.driver)
    context.mcq.verify_main_screen()

@when('User tap on Launch MCQ button')
def user_tap_on_launch_mcq_button(context):
    context.mcq = MCQ(context.obj.altdriver, context.obj.driver)
    context.mcq.clickMCQ()

@then('MCQ screen is loaded')
def mcq_screen_is_loaded(context):
    context.mcq = MCQ(context.obj.altdriver, context.obj.driver)
    context.mcq.verify_mcq_screen()

@step('MCQ question 1 is loaded')
def mcq_question_1_loaded(context):
    context.mcq = MCQ(context.obj.altdriver, context.obj.driver)
    context.mcq.verify_question_1()
    sleep(2)

@when('User taps on mcq option "{option}"')
def tap_on_mcq_option(context, option):
    context.mcq = MCQ(context.obj.altdriver, context.obj.driver)
    sleep(1)
    context.mcq.tap_option(option)

@then('MCQ question 2 not loaded')
def mcq_question_2_not_loaded(context):
    context.mcq = MCQ(context.obj.altdriver, context.obj.driver)
    context.mcq.verify_question_1()
    sleep(2)
        
@then('Pop up message should be displayed "{popup}"')
def verify_popup(context, popup):
    context.mcq = MCQ(context.obj.altdriver, context.obj.driver)
    context.mcq.verify_popup(popup)

@then('Verify animation "{option}"')
def verify_animation(context, option):
    context.mcq = MCQ(context.obj.altdriver, context.obj.driver)
    context.mcq.check_animation(option)

@step('MCQ question 2 is loaded')
def mcq_question_2_loaded(context):
    context.mcq = MCQ(context.obj.altdriver, context.obj.driver)
    context.mcq.verify_question_2()
    sleep(2)

@then('MCQ question 3 not loaded')
def mcq_question_3_not_loaded(context):
    context.mcq = MCQ(context.obj.altdriver, context.obj.driver)
    context.mcq.verify_question_2()

@step('MCQ question 3 is loaded')
def mcq_question_3_loaded(context):
    context.mcq = MCQ(context.obj.altdriver, context.obj.driver)
    context.mcq.verify_question_3()
    sleep(2)
'''
@given('MCQ question 1 is loaded')
def mcq_question_1_loaded(context):
    context.mcq = MCQ(context.obj.altdriver, context.obj.driver)
    context.mcq.verify_question_1()
    sleep(2)
    
@given('MCQ question 2 is loaded')
def mcq_question_2_loaded(context):
    context.mcq = MCQ(context.obj.altdriver, context.obj.driver)
    context.mcq.verify_question_2()
    sleep(2)
    
@given('MCQ question 3 is loaded')
def mcq_question_3_loaded(context):
    context.mcq = MCQ(context.obj.altdriver, context.obj.driver)
    context.mcq.verify_question_3()
    sleep(2)
'''    
    