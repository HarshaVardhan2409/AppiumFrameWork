@game_mcq
Feature: game_mcq

 Background: Launch game 
 Given game is launched:
 | game_name |
 | game_mcq  |
   
  
 Scenario: Check whether next question is loaded when wrong answer is selected for mcq question 1
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | mcq_four             | stage_001       |
    When select the option and verify:
    | option   | acceptable |
    | Option 2 | false      |
    | Option 3 | false      |
    | Option 4 | false      |
    
 Scenario: Check whether the pop up message is displaying when correct answer is selected for mcq question 1
   Given start scene is loaded
   And question is loaded:
   | object_with_question | question_number |
   | mcq_four             | stage_001       |
   When select the option and verify:
   | option   | acceptable |
   | Option 1 | true       |
   Then verify the popup message

