@perimater_mcq
Feature: perimater_mcq

 Background: Launch game 
 Given game is launched with text:
 | game_name       |
 | perimater_mcq |
 
 Scenario: Check whether next question is loaded when wrong answer is selected for mcq question 1
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_1         |
    When select the option and verify:
    | option   | acceptable |
    | Option_1 | false      |
    | Option_2 | false      |
    | Option_3 | false      |
    And question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_1         |
    
 @smoke1
 Scenario: Check whether next question is loaded when correct answer is selected for mcq question 1
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_1         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |
    And question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_2         |
    
 @smoke2
 Scenario: Check whether next question is loaded when wrong answer is selected for mcq question 2
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_1         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |
    And question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_2         |
    When select the option and verify:
    | option   | acceptable |
    | Option_1 | false      |
    | Option_2 | false      |
    | Option_3 | false      |
    
 @smoke3
 Scenario: Check whether next question is loaded when correct answer is selected for mcq question 2
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_1         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |
    And question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_2         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |
    And question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_3         |
    
 @smoke4
 Scenario: Check whether next question is loaded when wrong answer is selected for mcq question 3
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_1         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_2         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_3         |
    When select the option and verify:
    | option   | acceptable |
    | Option_1 | false      |
    | Option_2 | false      |
    | Option_3 | false      |
    
 @smoke4
 Scenario: Check whether next question is loaded when correct answer is selected for mcq question 3
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_1         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_2         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_3         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_4         |
    
 @smoke4
 Scenario: Check whether wrong answer is accepted for mcq question 4
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_1         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_2         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_3         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_4         |
    When select the option and verify:
    | option   | acceptable |
    | Option_1 | false      |
    | Option_2 | false      |
    | Option_3 | false      |
    
 @smoke4
 Scenario: Check whether correct answer is accepted for mcq question 4
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_1         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_2         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_3         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_4         |
    When select the option and verify:
    | option        | acceptable |
    | CorrectOption | true       |