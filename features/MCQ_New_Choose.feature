@mcq_g3mq24-mcq1_0_0
Feature: mcq_g3mq24-mcq1_0_0


Background: Launch game 
 Given game is launched with text and url:
 | game_name           |
 | mcq_g3mq24-mcq1_0_0 |
 
Scenario: check when a correct answer is selected for question 1 testrail details_3754_42
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question             | Stage_HKQg4m    |
And verify the text: "Helen is off to help advocate for the Supers." for element: "Intro1/TextTemplate"
When select the option and verify:  
| option        | acceptable |
| CorrectOption | true       |
Then update the result to testrail
