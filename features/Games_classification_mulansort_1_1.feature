@classification_mulansort_1_1
Feature: classification_mulansort_1_1


Background: Launch game 
 Given game is launched:
 | game_name             |
 | classification_mulansort_1_1 |

Scenario: check whether buckets are accepting the valid draggables for question 1 testrail details_1506_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_1 | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Ounces&DraggableObject_3Stage_1 | Bucket_Ounces&Bucket_1Stage_1 | true |
| Pounds&DraggableObject_2Stage_1 | Bucket_Pounds&Bucket_2Stage_1 | true |
| Stone&DraggableObject_1Stage_1 | Bucket_Stone&Bucket_3Stage_1 | true |
Then update the result to testrail

Scenario: check whether buckets are accepting the invalid draggables for question 1 testrail details_1507_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_1 | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Pounds&DraggableObject_2Stage_1 | Bucket_Ounces&Bucket_1Stage_1 | false |
| Stone&DraggableObject_1Stage_1 | Bucket_Ounces&Bucket_1Stage_1 | false |
| Stone&DraggableObject_1Stage_1 | Bucket_Pounds&Bucket_2Stage_1 | false |
|Ounces&DraggableObject_3Stage_1 | Bucket_Pounds&Bucket_2Stage_1 | false |
| Pounds&DraggableObject_2Stage_1 | Bucket_Stone&Bucket_3Stage_1 | false |
| Ounces&DraggableObject_3Stage_1 | Bucket_Stone&Bucket_3Stage_1 | false |
Then update the result to testrail

Scenario: check the animation of buckets by drag and drop the valid draggables for question 1 testrail details_1508_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_1 | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Ounces&DraggableObject_3Stage_1 | Bucket_Ounces&Bucket_1Stage_1 | true |
| Pounds&DraggableObject_2Stage_1 | Bucket_Pounds&Bucket_2Stage_1 | true |
| Stone&DraggableObject_1Stage_1 | Bucket_Stone&Bucket_3Stage_1 | true |
Then update the result to testrail

Scenario: check the animation of buckets by drag and drop the invalid draggables for question 1 testrail details_1509_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_1 | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Pounds&DraggableObject_2Stage_1 | Bucket_Ounces&Bucket_1Stage_1 | false |
| Stone&DraggableObject_1Stage_1 | Bucket_Ounces&Bucket_1Stage_1 | false |
| Stone&DraggableObject_1Stage_1 | Bucket_Pounds&Bucket_2Stage_1 | false |
| Ounces&DraggableObject_3Stage_1 | Bucket_Pounds&Bucket_2Stage_1 | false |
| Pounds&DraggableObject_2Stage_1 | Bucket_Stone&Bucket_3Stage_1 | false |
| Ounces&DraggableObject_3Stage_1 | Bucket_Stone&Bucket_3Stage_1 | false |
Then update the result to testrail

Scenario: check the text of question 1 on the screen testrail details_1510_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_1 | Stage_1 |
When verify the text
| question_text |
| Question&Passive_1Stage_1 |
Then update the result to testrail

Scenario: check the text message when correct answer is selected for question 1 testrail details_1511_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_1 | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Ounces&DraggableObject_3Stage_1 | Bucket_Ounces&Bucket_1Stage_1 | true |
| Pounds&DraggableObject_2Stage_1 | Bucket_Pounds&Bucket_2Stage_1 | true |
| Stone&DraggableObject_1Stage_1 | Bucket_Stone&Bucket_3Stage_1 | true |
Then update the result to testrail

Scenario: check whether buckets are accepting the valid draggables for question 2 testrail details_1512_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_1 | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Ounces&DraggableObject_3Stage_1 | Bucket_Ounces&Bucket_1Stage_1 | true |
| Pounds&DraggableObject_2Stage_1 | Bucket_Pounds&Bucket_2Stage_1 | true |
| Stone&DraggableObject_1Stage_1 | Bucket_Stone&Bucket_3Stage_1 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_2 | Stage_2 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Horse&DraggableObject_4Stage_2 | Bucket_Horsel&Bucket_1Stage_2 | true |
| Dog&DraggableObject_1Stage_2 | Bucket_Dog&Bucket_2Stage_2 | true |
| Hawk&DraggableObject_3Stage_2 | Bucket_Hawk&Bucket_3Stage_2 | true |
| Chick&DraggableObject_2Stage_2 | Bucket_Chickl&Bucket_4Stage_2 | true |
Then update the result to testrail

Scenario: check whether buckets are accepting the invalid draggables for question 2 testrail details_1513_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_1 | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Ounces&DraggableObject_3Stage_1 | Bucket_Ounces&Bucket_1Stage_1 | true |
| Pounds&DraggableObject_2Stage_1 | Bucket_Pounds&Bucket_2Stage_1 | true |
| Stone&DraggableObject_1Stage_1 | Bucket_Stone&Bucket_3Stage_1 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_2 | Stage_2 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Dog&DraggableObject_1Stage_2 | Bucket_Horsel&Bucket_1Stage_2 | false |
| Chick&DraggableObject_2Stage_2 | Bucket_Horsel&Bucket_1Stage_2 | false |
| Hawk&DraggableObject_3Stage_2 | Bucket_Horsel&Bucket_1Stage_2 | false |
| Chick&DraggableObject_2Stage_2 | Bucket_Dog&Bucket_2Stage_2 | false |
| Hawk&DraggableObject_3Stage_2 | Bucket_Dog&Bucket_2Stage_2 | false |
| Horse&DraggableObject_4Stage_2 | Bucket_Dog&Bucket_2Stage_2 | false |
| Dog&DraggableObject_1Stage_2 | Bucket_Hawk&Bucket_3Stage_2 | false |
| Chick&DraggableObject_2Stage_2 | Bucket_Hawk&Bucket_3Stage_2 | false |
| Horse&DraggableObject_4Stage_2 | Bucket_Hawk&Bucket_3Stage_2 | false |
| Dog&DraggableObject_1Stage_2 | Bucket_Chickl&Bucket_4Stage_2 | false |
| Hawk&DraggableObject_3Stage_2 | Bucket_Chickl&Bucket_4Stage_2 | false |
| Horse&DraggableObject_4Stage_2 | Bucket_Chickl&Bucket_4Stage_2 | false |
Then update the result to testrail

Scenario: check the animation of buckets by drag and drop the valid draggables for question 2 testrail details_1514_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_1 | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Ounces&DraggableObject_3Stage_1 | Bucket_Ounces&Bucket_1Stage_1 | true |
| Pounds&DraggableObject_2Stage_1 | Bucket_Pounds&Bucket_2Stage_1 | true |
| Stone&DraggableObject_1Stage_1 | Bucket_Stone&Bucket_3Stage_1 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_2 | Stage_2 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Horse&DraggableObject_4Stage_2 | Bucket_Horsel&Bucket_1Stage_2 | true |
| Dog&DraggableObject_1Stage_2 | Bucket_Dog&Bucket_2Stage_2 | true |
| Hawk&DraggableObject_3Stage_2 | Bucket_Hawk&Bucket_3Stage_2 | true |
| Chick&DraggableObject_2Stage_2 | Bucket_Chickl&Bucket_4Stage_2 | true |
Then update the result to testrail

Scenario: check the animation of buckets by drag and drop the invalid draggables for question 2 testrail details_1515_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_1 | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Ounces&DraggableObject_3Stage_1 | Bucket_Ounces&Bucket_1Stage_1 | true |
| Pounds&DraggableObject_2Stage_1 | Bucket_Pounds&Bucket_2Stage_1 | true |
| Stone&DraggableObject_1Stage_1 | Bucket_Stone&Bucket_3Stage_1 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_2 | Stage_2 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Dog&DraggableObject_1Stage_2 | Bucket_Horsel&Bucket_1Stage_2 | false |
| Chick&DraggableObject_2Stage_2 | Bucket_Horsel&Bucket_1Stage_2 | false |
| Hawk&DraggableObject_3Stage_2 | Bucket_Horsel&Bucket_1Stage_2 | false |
| Chick&DraggableObject_2Stage_2 | Bucket_Dog&Bucket_2Stage_2 | false |
| Hawk&DraggableObject_3Stage_2 | Bucket_Dog&Bucket_2Stage_2 | false |
| Horse&DraggableObject_4Stage_2 | Bucket_Dog&Bucket_2Stage_2 | false |
| Dog&DraggableObject_1Stage_2 | Bucket_Hawk&Bucket_3Stage_2 | false |
| Chick&DraggableObject_2Stage_2 | Bucket_Hawk&Bucket_3Stage_2 | false |
| Horse&DraggableObject_4Stage_2 | Bucket_Hawk&Bucket_3Stage_2 | false |
| Dog&DraggableObject_1Stage_2 | Bucket_Chickl&Bucket_4Stage_2 | false |
| Hawk&DraggableObject_3Stage_2 | Bucket_Chickl&Bucket_4Stage_2 | false |
| Horse&DraggableObject_4Stage_2 | Bucket_Chickl&Bucket_4Stage_2 | false |
Then update the result to testrail

Scenario: check the text of question 2 on the screen testrail details_1516_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_1 | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Ounces&DraggableObject_3Stage_1 | Bucket_Ounces&Bucket_1Stage_1 | true |
| Pounds&DraggableObject_2Stage_1 | Bucket_Pounds&Bucket_2Stage_1 | true |
| Stone&DraggableObject_1Stage_1 | Bucket_Stone&Bucket_3Stage_1 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_2 | Stage_2 |
When verify the text
| question_text |
| Question&Passive_1Stage_2 |
Then update the result to testrail

Scenario: check the text message when correct answer is selected for question 2 testrail details_1517_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_1 | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Ounces&DraggableObject_3Stage_1 | Bucket_Ounces&Bucket_1Stage_1 | true |
| Pounds&DraggableObject_2Stage_1 | Bucket_Pounds&Bucket_2Stage_1 | true |
| Stone&DraggableObject_1Stage_1 | Bucket_Stone&Bucket_3Stage_1 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_2 | Stage_2 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Horse&DraggableObject_4Stage_2 | Bucket_Horsel&Bucket_1Stage_2 | true |
| Dog&DraggableObject_1Stage_2 | Bucket_Dog&Bucket_2Stage_2 | true |
| Hawk&DraggableObject_3Stage_2 | Bucket_Hawk&Bucket_3Stage_2 | true |
| Chick&DraggableObject_2Stage_2 | Bucket_Chickl&Bucket_4Stage_2 | true |
Then update the result to testrail

Scenario: check whether user can able to complete the game by drag and drop the valid draggables testrail details_1518_29
Given start scene is loaded
And question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_1 | Stage_1 |
When drag and drop the draggables to bucket and verify position:
| draggable | bucket | acceptable |
| Ounces&DraggableObject_3Stage_1 | Bucket_Ounces&Bucket_1Stage_1 | true |
| Pounds&DraggableObject_2Stage_1 | Bucket_Pounds&Bucket_2Stage_1 | true |
| Stone&DraggableObject_1Stage_1 | Bucket_Stone&Bucket_3Stage_1 | true |
Then question is loaded:
| object_with_question | question_number |
| Question&Passive_1Stage_2 | Stage_2 |
When drag and drop the draggables to bucket and verify position:
| Horse&DraggableObject_4Stage_2 | Bucket_Horsel&Bucket_1Stage_2 | true |
| Dog&DraggableObject_1Stage_2 | Bucket_Dog&Bucket_2Stage_2 | true |
| Hawk&DraggableObject_3Stage_2 | Bucket_Hawk&Bucket_3Stage_2 | true |
| Chick&DraggableObject_2Stage_2 | Bucket_Chickl&Bucket_4Stage_2 | true |
Then update the result to testrail