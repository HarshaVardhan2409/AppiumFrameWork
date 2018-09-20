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
    When select the option:
    | option   | acceptable |
    | Option_1 | false      |
    | Option_2 | false      |
    | Option_3 | false      |
    Then verify animation
    And question is loaded:
    | object_with_question | question_number |
    | Question             | Stage_1         |