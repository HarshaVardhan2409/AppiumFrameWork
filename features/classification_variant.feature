@shapes_classification
Feature: shapes_classification

 Background: Launch game 
 Given game is launched:
 | game_name             |
 | shapes_classification |
 
 Scenario: Check whether bucket is accepting all the Triangle objects for classification question 1
    Given start scene is loaded
    And question is loaded:
    | draggable         | question_number |
    | DraggableObject_1 | Stage_1         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket | check_status | axis |
    | DraggableObject_1 | Box    | same         | y    |
    | DraggableObject_2 | Box    | same         | y    |
    
 Scenario: Check whether question 1 is completed by dragging the 2 valid and 1 invalid draggable objects for question 1
   Given start scene is loaded
   And question is loaded:
   | draggable         | question_number |
   | DraggableObject_1 | Stage_1         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | check_status | axis |
   | DraggableObject_3 | Box    | different    | y    |
   | DraggableObject_4 | Box    | different    | y    |
   | DraggableObject_1 | Box    | same         | y    |

 Scenario: Check whether bucket is accepting all the circle objects for question 1
   Given start scene is loaded
   And question is loaded:
   | draggable         | question_number |
   | DraggableObject_1 | Stage_1         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | check_status | axis |
   | DraggableObject_3 | Box    | different    | y    |
   | DraggableObject_4 | Box    | different    | y    |
   | DraggableObject_5 | Box    | different    | y    |
 
 Scenario: Check whether bucket is accepting all the circle objects for question 2
   Given start scene is loaded
   And question is loaded:
   | draggable         | question_number |
   | DraggableObject_1 | Stage_1         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | check_status | axis |
   | DraggableObject_3 | Box    | different    | y    |
   | DraggableObject_4 | Box    | different    | y    |
   | DraggableObject_5 | Box    | different    | y    |
   Then question is loaded:
   | draggable         | question_number |
   | DraggableObject_1 | Stage_2         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | check_status | axis |
   | DraggableObject_3 | Box    | same         | y    |
   | DraggableObject_4 | Box    | same         | y    |
   | DraggableObject_5 | Box    | same         | y    |
   
 Scenario: Check whether 2nd question is completed by dragging the 1 valid and 1 invalid draggable objects for question 2
   Given start scene is loaded
   And question is loaded:
   | draggable         | question_number |
   | DraggableObject_1 | Stage_1         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | check_status | axis |
   | DraggableObject_3 | Box    | different    | y    |
   | DraggableObject_4 | Box    | different    | y    |
   | DraggableObject_5 | Box    | different    | y    |
   Then question is loaded:
   | draggable         | question_number |
   | DraggableObject_1 | Stage_2         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | check_status | axis |
   | DraggableObject_1 | Box    | different    | y    |
   | DraggableObject_3 | Box    | same         | y    |
 
 @smoke  
 Scenario: Check whether bucket is accepting all the triangle objects for question 2
   Given start scene is loaded
   And question is loaded:
   | draggable         | question_number |
   | DraggableObject_1 | Stage_1         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | check_status | axis |
   | DraggableObject_3 | Box    | different    | y    |
   | DraggableObject_4 | Box    | different    | y    |
   | DraggableObject_5 | Box    | different    | y    |
   Then question is loaded:
   | draggable         | question_number |
   | DraggableObject_1 | Stage_2         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | check_status | axis |
   | DraggableObject_1 | Box    | same         | y    |
   | DraggableObject_2 | Box    | same         | y    |


