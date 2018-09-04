@mcq_variant
Feature: MCQ_Variant

  Scenario: Launch mcq game
    Given User is main page of the mcq application
    When User tap on Launch MCQ button
    Then MCQ screen is loaded
    And MCQ question 1 is loaded
    
  Scenario Outline: Check whether next question is loaded when wrong answer is selected for mcq question 1
    Given MCQ question 1 is loaded
    When User taps on mcq option "<option>"
    Then MCQ question 2 not loaded
    And Update mcq result to testrail "<caseID>"
    
    Examples: 
    | option   | caseID |
    | Option 2 | None   |
    | Option 3 | None   |
    | Option 4 | 194    |
    
  Scenario Outline: Check whether the pop up message is displaying when correct answer is selected for mcq question 1
    Given MCQ question 1 is loaded
    When User taps on mcq option "<option>"
    Then Pop up message should be displayed "<popup>"
    And Update mcq result to testrail "<caseID>"
    
    Examples:
    | option   | popup    | caseID |
    | Option 1 | Awesome! | 192    |

  Scenario: Relaunch the application
    Given Application is relaunched
    And User is main page of the mcq application
    When User tap on Launch MCQ button
    Then MCQ screen is loaded
    And MCQ question 1 is loaded
    
  Scenario Outline: Check the animation of option when correct answer is selected for question 1
    Given MCQ question 1 is loaded
    When User taps on mcq option "<option>"
    Then Verify animation "<option>"
    And Update mcq result to testrail "<caseID>"
    
    Examples:
    | option   | caseID |
    | Option 1 | 196    |
    
  Scenario: Relaunch the application
    Given Application is relaunched
    And User is main page of the mcq application
    When User tap on Launch MCQ button
    Then MCQ screen is loaded
    And MCQ question 1 is loaded
    
  Scenario Outline: Check whether next question is loaded when correct answer is selected for question 1
    Given MCQ question 1 is loaded
    When User taps on mcq option "<option>"
    Then MCQ question 2 is loaded
    And Update mcq result to testrail "<caseID>"
    
    Examples:
    | option   | caseID |
    | Option 1 | 193    |
    
  Scenario Outline: Check whether next question is loaded when wrong answer is selected for mcq question 2
    Given MCQ question 2 is loaded
    When User taps on mcq option "<option>"
    Then MCQ question 3 not loaded
    And Update mcq result to testrail "<caseID>"
    
    Examples: 
    | option   | caseID |
    | Option 2 | None   |
    | Option 3 | 200    |
    
  Scenario Outline: Check whether the pop up message is displaying when correct answer is selected for mcq question 2
    Given MCQ question 2 is loaded
    When User taps on mcq option "<option>"
    Then Pop up message should be displayed "<popup>"
    And Update mcq result to testrail "<caseID>"
    
    Examples:
    | option   | popup    | caseID |
    | Option 1 | Superb!  | 198    |
    
  Scenario: Relaunch the application
    Given Application is relaunched
    And User is main page of the mcq application
    When User tap on Launch MCQ button
    Then MCQ screen is loaded
    And MCQ question 1 is loaded
    
  Scenario Outline: Navigate to second question
    Given MCQ question 1 is loaded
    When User taps on mcq option "<option>"
    
    Examples:
    | option   |
    | Option 1 |
    
  Scenario Outline: Check the animation of option when correct answer is selected for question 2
    Given MCQ question 2 is loaded
    When User taps on mcq option "<option>"
    Then Verify animation "<option>"
    And Update mcq result to testrail "<caseID>"
    
    Examples: 
    | option   | caseID |
    | Option 1 | 204    |
    
  Scenario: Relaunch the application
    Given Application is relaunched
    And User is main page of the mcq application
    When User tap on Launch MCQ button
    Then MCQ screen is loaded
    And MCQ question 1 is loaded
    
  Scenario Outline: Navigate to second question
    Given MCQ question 1 is loaded
    When User taps on mcq option "<option>"
    
    Examples:
    | option   |
    | Option 1 |
  
  Scenario Outline: Check whether next question is loaded when correct answer is selected for question 2
    Given MCQ question 2 is loaded
    When User taps on mcq option "<option>"
    Then MCQ question 3 is loaded
    And Update mcq result to testrail "<caseID>"
    
    Examples: 
    | option   | caseID |
    | Option 1 | 199    |
    
  Scenario Outline: Check whether next question is loaded when wrong answer is selected for mcq question 3
    Given MCQ question 3 is loaded
    When User taps on mcq option "<option>"
    
    Examples:
    | option   |
    | Option 2 |
        
  Scenario Outline: Check whether the pop up message is displaying when correct answer is selected for mcq question 3
    Given MCQ question 3 is loaded
    When User taps on mcq option "<option>"
    Then Pop up message should be displayed "<popup>"
    And Verify animation "<option>"
    And Update mcq result to testrail "<caseID>"
    
    Examples:
    | option   | popup    | caseID |
    | Option 1 | Clever!  | 216    |
