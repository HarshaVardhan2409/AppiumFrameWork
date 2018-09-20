@mulansort_classification
Feature: mulansort_classification

 Background: Launch game 
 Given game is launched with text:
 | game_name                |
 | mulansort_classification |
 
 @invalid
 Scenario: Check whether bucket is accepting all the invalid draggable objects for classification question 1
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_1         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket        | acceptable |
    | DraggableObject_2 | Bucket_Ounces | false      |
    | DraggableObject_1 | Bucket_Pounds | false      |
    | DraggableObject_3 | Bucket_Stone  | false      |
    
 @smoke
 Scenario: Check whether bucket is accepting all the valid draggable objects for classification question 1
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_1         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket        | acceptable |
    | DraggableObject_3 | Bucket_Ounces | true       |
    | DraggableObject_2 | Bucket_Pounds | true       |
    | DraggableObject_1 | Bucket_Stone  | true       |
    And question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_2         |