@shapes_classification
Feature: shapes_classification

 Background: Launch game 
 Given game is launched:
 | game_name            |
 | shapes_classification|
 
 Scenario: Check whether bucket is accepting all the Triangle objects for classification question 1
    Given start scene is loaded
    When drag and drop the draggables to bucket:
    | draggable         | bucket |
    | DraggableObject_1 | Box    |
    | DraggableObject_2 | Box    |
 
