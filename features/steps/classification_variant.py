from time import sleep
import sys

from ..games.templetes.classification import Classification
sys.path.append('../generics/')
import test_management
import generics_lib
import constants

start_y = None
end_y = None
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
    sleep(5)
    #game_name = str(context.feature.name)
    context.classify.wait_for_scene(generics_lib.get_data(constants.classification_path, context.feature.name, "start_screen"))

    
@step('drag and drop the draggables to bucket')
def drag_and_drop_the_draggables_to_bucket(context):
    context.classify = Classification(context.obj.altdriver, context.obj.driver)
    for row in context.table:
        sleep(3)
        context.classify.drag_object_to_bucket(row['draggable'], row['bucket'])

