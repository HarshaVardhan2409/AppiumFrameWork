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
    Then question is loaded:
    | object_with_question | question_number |
    | mcq_four             | stage_001       |
    
 Scenario: Check animation of option and the level successful message is displaying when correct answer is selected for mcq question 1
   Given start scene is loaded
   And question is loaded:
   | object_with_question | question_number |
   | mcq_four             | stage_001       |
   When select the option and verify:
   | option   | acceptable |
   | Option 1 | true       |
   Then verify the level successful message:
   | object_name       | text     |
   | GratificationText | Awesome! |

 Scenario: Check whether next question is loaded when correct answer is selected for question 1
   Given start scene is loaded
   And question is loaded:
   | object_with_question | question_number |
   | mcq_four             | stage_001       |
   When select the option and verify:
   | option   | acceptable |
   | Option 1 | true       |
   Then question is loaded:
   | object_with_question | question_number |
   | mcq_four             | stage_002       |
   
 Scenario: Check whether next question is loaded when wrong answer is selected for mcq question 2
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | mcq_four             | stage_001       |
    When select the option and verify:
    | option   | acceptable |
    | Option 1 | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | mcq_four             | stage_002       |
    When select the option and verify:
    | option   | acceptable |
    | Option 2 | false      |
    | Option 3 | false      |
    Then question is loaded:
    | object_with_question | question_number |
    | mcq_four             | stage_002       |
    
 Scenario: Check animation of option and the level successful message is displaying when correct answer is selected for mcq question 2
   Given start scene is loaded
   And question is loaded:
    | object_with_question | question_number |
    | mcq_four             | stage_001       |
   When select the option and verify:
   | option   | acceptable |
   | Option 1 | true       |
   Then question is loaded:
    | object_with_question | question_number |
    | mcq_four             | stage_002       |
   When select the option and verify:
   | option   | acceptable |
   | Option 1 | true       | 
   Then verify the level successful message:
   | object_name       | text     |
   | GratificationText | Superb!  |

 Scenario: Check whether next question is loaded when correct answer is selected for question 2
   Given start scene is loaded
   And question is loaded:
    | object_with_question | question_number |
    | mcq_four             | stage_001       |
   When select the option and verify:
   | option   | acceptable |
   | Option 1 | true       |
   Then question is loaded:
   | object_with_question | question_number |
   | mcq_four             | stage_002       |
   When select the option and verify:
   | option   | acceptable |
   | Option 1 | true       |
   Then question is loaded:
   | object_with_question | question_number |
   | mcq_four             | stage_003       |
  
 Scenario: Check whether wrong answer is accepted as correct for mcq question 3
    Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | mcq_four             | stage_001       |
    When select the option and verify:
    | option   | acceptable |
    | Option 1 | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | mcq_four             | stage_002       |
    When select the option and verify:
    | option   | acceptable |
    | Option 1 | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | mcq_four             | stage_003       |
    When select the option and verify:
    | option   | acceptable |
    | Option 2 | false      |
    
 Scenario: Check animation of option and the level successful message is displaying when correct answer is selected for mcq question 3
   Given start scene is loaded
    And question is loaded:
    | object_with_question | question_number |
    | mcq_four             | stage_001       |
    When select the option and verify:
    | option   | acceptable |
    | Option 1 | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | mcq_four             | stage_002       |
    When select the option and verify:
    | option   | acceptable |
    | Option 1 | true       |
    Then question is loaded:
    | object_with_question | question_number |
    | mcq_four             | stage_003       |
    When select the option and verify:
    | option   | acceptable |
    | Option 1 | true       | 
   Then verify the level successful message:
   | object_name       | text     |
   | GratificationText | Clever!  |