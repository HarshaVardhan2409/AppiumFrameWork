@Games
Feature: Games


Background: Launch game 
 Given game is launched with text:
 | game_name             |
 | classification_mulan_classification_1_1 |

Scenario: check whether buckets are accepting the valid draggables for question 1 testrail details_1585_20
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Header_question&Passive_1Common_Stage | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Flag_1&DraggableObject_1Stage_1 | Bucket_Customary&Bucket_2Stage_1 | true |
| Flag_2&DraggableObject_2Stage_1 | Bucket_Metric&Bucket_1Stage_1 | true |
Then update the result to testrail

Scenario: check whether buckets are accepting the invalid draggables for question 1 testrail details_1586_20
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Header_question&Passive_1Common_Stage | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Flag_2&DraggableObject_2Stage_1 | Bucket_Customary&Bucket_2Stage_1 | false |
| Flag_1&DraggableObject_1Stage_1 | Bucket_Metric&Bucket_1Stage_1 | false |
Then update the result to testrail

Scenario: check the text of question 1 on the screen testrail details_1589_20
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Header_question&Passive_1Common_Stage | Stage_1 |
When verify the text:
| object_name |
| Header_question&Passive_1Common_Stage |
Then update the result to testrail

Scenario: check whether buckets are accepting the valid draggables for question 2 testrail details_1590_20
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Header_question&Passive_1Common_Stage | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Flag_1&DraggableObject_1Stage_1 | Bucket_Customary&Bucket_2Stage_1 | true |
| Flag_2&DraggableObject_2Stage_1 | Bucket_Metric&Bucket_1Stage_1 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_5Common_Stage | Stage_2 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Stone_2&DraggableObject_2Stage_2 | Bucket_Customary&Bucket_2Stage_2 | true |
| Stone_4&DraggableObject_4Stage_2 | Bucket_Customary&Bucket_2Stage_2 | true |
| Stone_1&DraggableObject_1Stage_2 | Bucket_Metric&Bucket_1Stage_2 | true |
| Stone_3&DraggableObject_3Stage_2 | Bucket_Metric&Bucket_1Stage_2 | true |
Then update the result to testrail

Scenario: check whether buckets are accepting the invalid draggables for question 2 testrail details_1591_20
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Header_question&Passive_1Common_Stage | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Flag_1&DraggableObject_1Stage_1 | Bucket_Customary&Bucket_2Stage_1 | true |
| Flag_2&DraggableObject_2Stage_1 | Bucket_Metric&Bucket_1Stage_1 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_5Common_Stage | Stage_2 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Stone_1&DraggableObject_1Stage_2 | Bucket_Customary&Bucket_2Stage_2 | false |
| Stone_3&DraggableObject_3Stage_2 | Bucket_Customary&Bucket_2Stage_2 | false |
| Stone_2&DraggableObject_2Stage_2 | Bucket_Metric&Bucket_1Stage_2 | false |
| Stone_4&DraggableObject_4Stage_2 | Bucket_Metric&Bucket_1Stage_2 | false |
Then update the result to testrail

Scenario: check the text of question 2 on the screen testrail details_1594_20
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Header_question&Passive_1Common_Stage | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Flag_1&DraggableObject_1Stage_1 | Bucket_Customary&Bucket_2Stage_1 | true |
| Flag_2&DraggableObject_2Stage_1 | Bucket_Metric&Bucket_1Stage_1 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_5Common_Stage | Stage_2 |
When verify the text:
| object_name |
| Question&Passive_5Common_Stage |
Then update the result to testrail

Scenario: check whether buckets are accepting the valid draggables for question 3 testrail details_1595_20
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Header_question&Passive_1Common_Stage | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Flag_1&DraggableObject_1Stage_1 | Bucket_Customary&Bucket_2Stage_1 | true |
| Flag_2&DraggableObject_2Stage_1 | Bucket_Metric&Bucket_1Stage_1 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_5Common_Stage | Stage_2 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Stone_2&DraggableObject_2Stage_2 | Bucket_Customary&Bucket_2Stage_2 | true |
| Stone_4&DraggableObject_4Stage_2 | Bucket_Customary&Bucket_2Stage_2 | true |
| Stone_1&DraggableObject_1Stage_2 | Bucket_Metric&Bucket_1Stage_2 | true |
| Stone_3&DraggableObject_3Stage_2 | Bucket_Metric&Bucket_1Stage_2 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_5Common_Stage | Stage_3 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Stone_1&DraggableObject_1Stage_3 | Bucket_Customary&Bucket_1Stage_3 | true |
| Stone_2&DraggableObject_2Stage_3 | Bucket_Customary&Bucket_1Stage_3 | true |
| Stone_3&DraggableObject_3Stage_3 | Bucket_Metric&Bucket_2Stage_3 | true |
| Stone_4&DraggableObject_4Stage_3 | Bucket_Metric&Bucket_2Stage_3 | true |
Then update the result to testrail

Scenario: check whether buckets are accepting the invalid draggables for question 3 testrail details_1596_20
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Header_question&Passive_1Common_Stage | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Flag_1&DraggableObject_1Stage_1 | Bucket_Customary&Bucket_2Stage_1 | true |
| Flag_2&DraggableObject_2Stage_1 | Bucket_Metric&Bucket_1Stage_1 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_5Common_Stage | Stage_2 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Stone_2&DraggableObject_2Stage_2 | Bucket_Customary&Bucket_2Stage_2 | true |
| Stone_4&DraggableObject_4Stage_2 | Bucket_Customary&Bucket_2Stage_2 | true |
| Stone_1&DraggableObject_1Stage_2 | Bucket_Metric&Bucket_1Stage_2 | true |
| Stone_3&DraggableObject_3Stage_2 | Bucket_Metric&Bucket_1Stage_2 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_5Common_Stage | Stage_3 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Stone_3&DraggableObject_3Stage_3 | Bucket_Customary&Bucket_1Stage_3 | false |
| Stone_4&DraggableObject_4Stage_3 | Bucket_Customary&Bucket_1Stage_3 | false |
| Stone_1&DraggableObject_1Stage_3 | Bucket_Metric&Bucket_2Stage_3 | false |
| Stone_2&DraggableObject_2Stage_3 | Bucket_Metric&Bucket_2Stage_3 | false |
Then update the result to testrail

Scenario: check the text of question 3 on the screen testrail details_1599_20
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Header_question&Passive_1Common_Stage | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Flag_1&DraggableObject_1Stage_1 | Bucket_Customary&Bucket_2Stage_1 | true |
| Flag_2&DraggableObject_2Stage_1 | Bucket_Metric&Bucket_1Stage_1 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_5Common_Stage | Stage_2 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Stone_2&DraggableObject_2Stage_2 | Bucket_Customary&Bucket_2Stage_2 | true |
| Stone_4&DraggableObject_4Stage_2 | Bucket_Customary&Bucket_2Stage_2 | true |
| Stone_1&DraggableObject_1Stage_2 | Bucket_Metric&Bucket_1Stage_2 | true |
| Stone_3&DraggableObject_3Stage_2 | Bucket_Metric&Bucket_1Stage_2 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_5Common_Stage | Stage_3 |
When verify the text:
| object_name |
| Question&Passive_5Common_Stage |
Then update the result to testrail

Scenario: check whether user can able to complete the game by drag and drop the valid draggables testrail details_1600_20
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Header_question&Passive_1Common_Stage | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Flag_1&DraggableObject_1Stage_1 | Bucket_Customary&Bucket_2Stage_1 | true |
| Flag_2&DraggableObject_2Stage_1 | Bucket_Metric&Bucket_1Stage_1 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_5Common_Stage | Stage_2 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Stone_2&DraggableObject_2Stage_2 | Bucket_Customary&Bucket_2Stage_2 | true |
| Stone_4&DraggableObject_4Stage_2 | Bucket_Customary&Bucket_2Stage_2 | true |
| Stone_1&DraggableObject_1Stage_2 | Bucket_Metric&Bucket_1Stage_2 | true |
| Stone_3&DraggableObject_3Stage_2 | Bucket_Metric&Bucket_1Stage_2 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_5Common_Stage | Stage_3 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Stone_1&DraggableObject_1Stage_3 | Bucket_Customary&Bucket_1Stage_3 | true |
| Stone_2&DraggableObject_2Stage_3 | Bucket_Customary&Bucket_1Stage_3 | true |
| Stone_3&DraggableObject_3Stage_3 | Bucket_Metric&Bucket_2Stage_3 | true |
| Stone_4&DraggableObject_4Stage_3 | Bucket_Metric&Bucket_2Stage_3 | true |
Then update the result to testrail