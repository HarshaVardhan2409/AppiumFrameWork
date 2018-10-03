@Games
Feature: Games


Background: Launch game 
 Given game is launched with text:
 | game_name             |
 | mcq_peri-mater_maths_0_0 |

Scenario: check when a correct answer is selected for question 1
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then update the result to testrail: case 1601 : suite 30

Scenario: check when incorrect answer is selected for question 1
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:
| option | acceptable |
| WrongOption_1 | false |
| WrongOption_2 | false |
| WrongOption_3 | false |
Then update the result to testrail: case 1602 : suite 30

Scenario: check the text of question 1 on the screen
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When verify the text:
| object_name |
| Question |
Then update the result to testrail: case 1603 : suite 30

Scenario: check the text message when correct answer is selected for question 1
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question | Stage_1 |
When select the option and verify:  
| option | acceptable |
| CorrectOption | true |
Then update the result to testrail: case 1604 : suite 30

Scenario: check when a correct answer is selected for question 2
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
Then update the result to testrail: case 1605 : suite 30

Scenario: check when incorrect answer is selected for question 2
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
Then update the result to testrail: case 1606 : suite 30

Scenario: check the text of question 2 on the screen
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
Then update the result to testrail: case 1607 : suite 30

Scenario: check the text message when correct answer is selected for question 2
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
Then update the result to testrail: case 1608 : suite 30

Scenario: check when a correct answer is selected for question 3
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
Then update the result to testrail: case 1609 : suite 30

Scenario: check when incorrect answer is selected for question 3
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
Then update the result to testrail: case 1610 : suite 30

Scenario: check the text of question 3 on the screen
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
Then update the result to testrail: case 1611 : suite 30

Scenario: check the text message when correct answer is selected for question 3
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
Then update the result to testrail: case 1612 : suite 30

Scenario: check when a correct answer is selected for question 4
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
Then update the result to testrail: case 1613 : suite 30

Scenario: check when incorrect answer is selected for question 4
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
Then update the result to testrail: case 1614 : suite 30

Scenario: check the text of question 4 on the screen
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
Then update the result to testrail: case 1615 : suite 30

Scenario: check the text message when correct answer is selected for question 4
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
Then update the result to testrail: case 1616 : suite 30

Scenario: check whether user can able to complete the game by selecting the correct answers
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
Then update the result to testrail: case 1617 : suite 30