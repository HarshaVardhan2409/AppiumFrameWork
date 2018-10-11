@classification_mulan_classification_1_1
Feature: classification_mulan_classification_1_1


Background: Launch game 
 Given game is launched with text:
 | game_name             |
 | classification_mulan_classification_1_1 |

Scenario: check whether buckets are accepting the valid draggables for question 1 testrail details_1585_29
Given capture the app logs for: "com.byjus.k3"
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Header_question | Stage_1 |
And verify the text "Drag the units to their matching systems of measurement." for element: Header_question
And verify the multiple texts:
| object_with_text | text      |
| CustomaryTitle   | Customary |
| MetricTitle      | Metric    |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| DraggableObject_1 | Bucket_2 | true |
| DraggableObject_2 | Bucket_1 | true |
Then update the result to testrail

Scenario: check whether buckets are accepting the invalid draggables for question 1 testrail details_1586_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Header_question | Stage_1 |
And verify the text "Drag the units to their matching systems of measurement." for element: Header_question
And verify the multiple texts:
| object_with_text | text      |
| CustomaryTitle   | Customary |
| MetricTitle      | Metric    |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| DraggableObject_2 | Bucket_2 | false |
| DraggableObject_1 | Bucket_1 | false |
Then update the result to testrail