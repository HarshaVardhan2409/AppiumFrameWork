@mulan_classification
Feature: mulan_classification

 Background: Launch game 
 Given game is launched with text:
 | game_name             |
 | mulan_classification  |
 
 Scenario: Check whether bucket is accepting all the invalid draggable objects for classification question 1
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_1         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket           | acceptable |
    | DraggableObject_1 | Bucket_Metric    | false      |
    | DraggableObject_2 | Bucket_Customary | false      |

 Scenario: Check whether bucket is accepting all the valid draggable objects for classification question 1
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_1         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket              | acceptable |
    | DraggableObject_1 | Bucket_Customary    | true       |
    | DraggableObject_2 | Bucket_Metric       | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_2         |
    
 Scenario: Check whether bucket is accepting all the invalid draggable objects for classification question 2
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_1         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket              | acceptable |
    | DraggableObject_1 | Bucket_Customary    | true       |
    | DraggableObject_2 | Bucket_Metric       | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_2         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket              | acceptable |
    | DraggableObject_2 | Bucket_Metric       | false      |
    | DraggableObject_4 | Bucket_Metric       | false      |
    | DraggableObject_1 | Bucket_Customary    | false      |
    | DraggableObject_3 | Bucket_Customary    | false      |
    
 Scenario: Check whether bucket is accepting all the valid draggable objects for classification question 2
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_1         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket              | acceptable |
    | DraggableObject_1 | Bucket_Customary    | true       |
    | DraggableObject_2 | Bucket_Metric       | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_2         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket              | acceptable |
    | DraggableObject_2 | Bucket_Customary    | true       |
    | DraggableObject_4 | Bucket_Customary    | true       |
    | DraggableObject_1 | Bucket_Metric       | true       |
    | DraggableObject_3 | Bucket_Metric       | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_3         |
    
 Scenario: Check whether bucket is accepting all the invalid draggable objects for classification question 3
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_1         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket              | acceptable |
    | DraggableObject_1 | Bucket_Customary    | true       |
    | DraggableObject_2 | Bucket_Metric       | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_2         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket              | acceptable |
    | DraggableObject_2 | Bucket_Customary    | true       |
    | DraggableObject_4 | Bucket_Customary    | true       |
    | DraggableObject_1 | Bucket_Metric       | true       |
    | DraggableObject_3 | Bucket_Metric       | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_3         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket              | acceptable |
    | DraggableObject_1 | Bucket_Metric       | false      |
    | DraggableObject_2 | Bucket_Metric       | false      |
    | DraggableObject_3 | Bucket_Customary    | false      |
    | DraggableObject_4 | Bucket_Customary    | false      |
    
 Scenario: Check whether bucket is accepting all the valid draggable objects for classification question 3 and animation for game completion
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_1         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket              | acceptable |
    | DraggableObject_1 | Bucket_Customary    | true       |
    | DraggableObject_2 | Bucket_Metric       | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_2         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket              | acceptable |
    | DraggableObject_2 | Bucket_Customary    | true       |
    | DraggableObject_4 | Bucket_Customary    | true       |
    | DraggableObject_1 | Bucket_Metric       | true       |
    | DraggableObject_3 | Bucket_Metric       | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | DraggableObject_1    | Stage_3         |
    When drag and drop the draggables to bucket and verify position:
    | draggable         | bucket              | acceptable |
    | DraggableObject_1 | Bucket_Customary    | true       |
    | DraggableObject_2 | Bucket_Customary    | true       |
    | DraggableObject_3 | Bucket_Metric       | true       |
    | DraggableObject_4 | Bucket_Metric       | true       |