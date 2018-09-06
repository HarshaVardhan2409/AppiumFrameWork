from time import sleep
import sys

from ..games.templates.classification.classification import Classification

sys.path.append('../generics/')
import generics_lib
import constants

start_position = None
end_position = None
game_name = None

@step('game is launched')
def game_is_launched(context):
    for row in context.table:
        game_name = row["game_name"]
    context.classify = Classification(context.obj.altdriver, context.obj.driver)
    context.classify.wait_for_scene(generics_lib.get_data(constants.classification_path, game_name, "launch_screen"))
    context.classify.start_game(generics_lib.get_data(constants.classification_path, game_name, "launch_game"))
    

@step('start scene is loaded')
def start_scene_is_loaded(context):
    context.classify = Classification(context.obj.altdriver, context.obj.driver)
    context.classify.wait_for_scene(generics_lib.get_data(constants.classification_path, context.feature.name, "start_screen"))

@step('question is loaded')
def question_is_loaded(context):
    context.classify = Classification(context.obj.altdriver, context.obj.driver)
    for row in context.table:
        context.classify.verify_question(row["draggable"], row["question_number"])
    
    
@step('drag and drop the draggables to bucket and verify position')
def drag_and_drop_the_draggables_to_bucket(context):
    context.classify = Classification(context.obj.altdriver, context.obj.driver)
    for row in context.table:
        #wait time for elements to appear on the screen
        sleep(2)
        start_position = context.classify.get_object_location(row["draggable"])
        context.classify.drag_object_to_bucket(row['draggable'], row['bucket'])
        
        sleep(1)
        end_position = context.classify.get_object_location(row["draggable"])
        if 'x' in row["axis"]:
            context.classify.verify_object_location(start_position['x'], end_position['x'], row['check_status'])
        elif 'y' in row['axis']:
            context.classify.verify_object_location(start_position['y'], end_position['y'], row['check_status'])

