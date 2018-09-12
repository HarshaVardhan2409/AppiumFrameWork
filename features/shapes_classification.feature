@shapes_classification
Feature: shapes_classification

 Background: Launch game 
 Given game is launched:
 | game_name             |
 | shapes_classification |
 
 Scenario: Check whether bucket is accepting all the invalid draggable objects for classification question 1
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_1         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket | acceptable |
    | DraggableObject_1 | Box    | false      |
    | DraggableObject_2 | Box    | false      |
    
 Scenario: Check whether question 1 is completed by dragging the 2 valid and 1 invalid draggable objects for question 1
   Given start scene is loaded
   And question is loaded:
   | object_with_question | question_number |
   | DraggableObject_1    | Stage_1         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | acceptable |
   | DraggableObject_3 | Box    | true    	 |
   | DraggableObject_4 | Box    | true    	 |
   | DraggableObject_1 | Box    | false      |

 Scenario: Check whether bucket is accepting all the circle objects for question 1
   Given start scene is loaded
   And question is loaded:
   | object_with_question | question_number |
   | DraggableObject_1    | Stage_1         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | acceptable |
   | DraggableObject_3 | Box    | true    	 |
   | DraggableObject_4 | Box    | true     	 |
   | DraggableObject_5 | Box    | true    	 |
 
 Scenario: Check whether bucket is accepting all the circle objects for question 2
   Given start scene is loaded
   And question is loaded:
   | object_with_question | question_number |
   | DraggableObject_1    | Stage_1         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | acceptable |
   | DraggableObject_3 | Box    | true    	 |
   | DraggableObject_4 | Box    | true    	 |
   | DraggableObject_5 | Box    | true    	 |
   Then question is loaded:
   | object_with_question | question_number |
   | DraggableObject_1    | Stage_2         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | acceptable |
   | DraggableObject_3 | Box    | false      |
   | DraggableObject_4 | Box    | false      |
   | DraggableObject_5 | Box    | false      |
   
 Scenario: Check whether 2nd question is completed by dragging the 1 valid and 1 invalid draggable objects for question 2
   Given start scene is loaded
   And question is loaded:
   | object_with_question | question_number |
   | DraggableObject_1    | Stage_1         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | acceptable |
   | DraggableObject_3 | Box    | true    	 |
   | DraggableObject_4 | Box    | true    	 |
   | DraggableObject_5 | Box    | true    	 |
   Then question is loaded:
   | object_with_question | question_number |
   | DraggableObject_1    | Stage_2         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | acceptable |
   | DraggableObject_1 | Box    | true    	 |
   | DraggableObject_3 | Box    | false      |
 
 @smoke  
 Scenario: Check whether bucket is accepting all the triangle objects for question 2
   Given start scene is loaded
   And question is loaded:
   | object_with_question | question_number |
   | DraggableObject_1    | Stage_1         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | acceptable |
   | DraggableObject_3 | Box    | true    	 |
   | DraggableObject_4 | Box    | true    	 |
   | DraggableObject_5 | Box    | true    	 |
   Then question is loaded:
   | object_with_question | question_number |
   | DraggableObject_1    | Stage_2         |
   When drag and drop the draggables to bucket and verify position:
   | draggable         | bucket | acceptable |
   | DraggableObject_1 | Box    | true       |
   | DraggableObject_2 | Box    | true       |


