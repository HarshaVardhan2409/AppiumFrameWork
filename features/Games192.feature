@Games
Feature: Games


Background: Launch game 
 Given game is launched with text:
 | game_name             |
 | classification_mulan_classification_1_1 |

Scenario: check whether buckets are accepting the valid draggables for question 1
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Header_question&Passive_1Common_Stage | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| DraggableObject_1 | Bucket_Customary | true |
| DraggableObject_2 | Bucket_Metric    | true |
Then update the result to testrail: case 1585 : suite 29