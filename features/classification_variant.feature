@classification_variant
Feature: Classification_Variant

  @smoke
  @regression
  Scenario: Launch classification game
    Given User is main page of the classification application
    When User tap on Launch Classification button
    Then Classification screen is loaded
    And All the classification objects are loaded
    
  @smoke
  @regression
  Scenario Outline: Check whether bucket is accepting all the Triangle objects for classification question 1
    Given Classification question 1 is loaded
    When User drag and drop the classification "<draggable>" to the bucket
    Then Verify the classification "<draggable>"
    And Update classification result to testrail "<caseID>"

    Examples:
    | draggable         | caseID |
    | DraggableObject_1 | None   |
    | DraggableObject_2 | 181    |

  @smoke
  @regression
  Scenario Outline: Check whether user is able to complete the 1st question by dragging the 2 valid and 1 invalid draggable objects for question 1
    Given Classification question 1 is loaded
    When User drag and drop the classification "<draggable>" to the bucket
    Then Verify the classification "<draggable>"
    And Update classification result to testrail "<caseID>"

    Examples:
    | draggable         | caseID |
    | DraggableObject_3 | None   |
    | DraggableObject_4 | None   |
    | DraggableObject_1 | 185    |

  @regression
  Scenario: Relaunch the application
    Given Application is relaunched
    And User is main page of the classification application
    When User tap on Launch Classification button
    Then Classification screen is loaded
    And All the classification objects are loaded

  @regression
  Scenario Outline: Check whether bucket is accepting all the circle objects for question 1
    Given Classification question 1 is loaded
    When User drag and drop the classification "<draggable>" to the bucket
    Then Verify the classification "<draggable>"
    And Update classification result to testrail "<caseID>"

    Examples:
    | draggable         | caseID |
    | DraggableObject_3 | None   |
    | DraggableObject_4 | None   |
    | DraggableObject_5 | 180    |
    
  @regression
  Scenario Outline: Check whether bucket is accepting all the circle objects for question 2
    Given Classification question 2 is loaded
    When User drag and drop the classification "<draggable>" to the bucket
    Then Verify the classification "<draggable>"
    And Update classification result to testrail "<caseID>"

    Examples:
    | draggable         | caseID |
    | DraggableObject_3 | None   |
    | DraggableObject_4 | None   |
    | DraggableObject_5 | 187    |
  
  @regression  
  Scenario Outline: Check whether user is able to complete the 2nd question by dragging the 1 valid and 1 invalid draggable objects for question 2
    Given Classification question 2 is loaded
    When User drag and drop the classification "<draggable>" to the bucket
    Then Verify the classification "<draggable>"
    And Update classification result to testrail "<caseID>"
    
    Examples:
    | draggable         | caseID |
    | DraggableObject_1 | None   |
    | DraggableObject_3 | 189    |
  @regression
  Scenario: Relaunch the application
    Given Application is relaunched
    And User is main page of the classification application
    When User tap on Launch Classification button
    Then Classification screen is loaded
    And All the classification objects are loaded
  
  @regression
  Scenario Outline: Complete question 1
    Given Classification question 1 is loaded
    When User drag and drop the classification "<draggable>" to the bucket
    Then Verify the classification "<draggable>"

    Examples:
    | draggable         |
    | DraggableObject_3 |
    | DraggableObject_4 |
    | DraggableObject_5 |
    
  @regression_1
  Scenario Outline: Check whether bucket is accepting all the triangle objects for question 2
    Given Classification question 2 is loaded
    When User drag and drop the classification "<draggable>" to the bucket
    Then Verify the classification "<draggable>"
    And Update classification result to testrail "<caseID>"
    
    Examples:
    | draggable         | caseID |
    | DraggableObject_1 | None   |
    | DraggableObject_2 | 186    |
 
