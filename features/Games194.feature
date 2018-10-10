@Games
Feature: Games


Background: Launch game 
 Given game is launched with text:
 | game_name             |
 | mcq_peri-mater_maths_0_0 |

Scenario: check when a correct answer is selected for question 1 testrail details_1601_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then update the result to testrail

Scenario: check when incorrect answer is selected for question 1 testrail details_1602_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:
| option | acceptable |
| WrongOption_1 | false |
| WrongOption_2 | false |
| WrongOption_3 | false |
Then update the result to testrail

Scenario: check the text of question 1 on the screen testrail details_1603_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When verify the text:
| object_name |
| Question |
Then update the result to testrail

Scenario: check the text message when correct answer is selected for question 1 testrail details_1604_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then update the result to testrail

Scenario: check when a correct answer is selected for question 2 testrail details_1605_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_2 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then update the result to testrail

Scenario: check when incorrect answer is selected for question 2 testrail details_1606_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_2 |
When select the option and verify:
| option | acceptable |
| WrongOption_1 | false |
| WrongOption_2 | false |
| WrongOption_3 | false |
Then update the result to testrail

Scenario: check the text of question 2 on the screen testrail details_1607_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_2 |
When verify the text:
| object_name | 
| Question |
Then update the result to testrail

Scenario: check the text message when correct answer is selected for question 2 testrail details_1608_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_2 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then update the result to testrail

Scenario: check when a correct answer is selected for question 3 testrail details_1609_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_2 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_3 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then update the result to testrail

Scenario: check when incorrect answer is selected for question 3 testrail details_1610_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_2 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_3 |
When select the option and verify:
| option | acceptable |
| WrongOption_1 | false |
| WrongOption_2 | false |
| WrongOption_3 | false |
Then update the result to testrail

Scenario: check the text of question 3 on the screen testrail details_1611_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_2 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_3 |
When verify the text:
| object_name | 
| Question |
Then update the result to testrail

Scenario: check the text message when correct answer is selected for question 3 testrail details_1612_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_2 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_3 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then update the result to testrail

Scenario: check when a correct answer is selected for question 4 testrail details_1613_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_2 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_3 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_4 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then update the result to testrail

Scenario: check when incorrect answer is selected for question 4 testrail details_1614_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_2 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_3 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_4 |
When select the option and verify:
| option | acceptable |
| WrongOption_1 | false |
| WrongOption_2 | false |
| WrongOption_3 | false |
Then update the result to testrail

Scenario: check the text of question 4 on the screen testrail details_1615_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_2 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_3 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_4 |
When verify the text:
| object_name | 
| Question |
Then update the result to testrail

Scenario: check the text message when correct answer is selected for question 4 testrail details_1616_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_2 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_3 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_4 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then update the result to testrail

Scenario: check whether user can able to complete the game by selecting the correct answers testrail details_1617_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_2 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_3 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then question is loaded:
| object_with_question | question_number |
| Question | Stage_4 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then update the result to testrail