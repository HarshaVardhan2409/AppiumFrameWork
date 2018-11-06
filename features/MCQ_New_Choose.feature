@mcq_g3mq24-mcq1_0_0
Feature: mcq_g3mq24-mcq1_0_0


Background: Launch game 
 Given game is launched with text and url:
 | game_name           |
 | mcq_g3mq24-mcq1_0_0 |
 
Scenario: check when a correct answer is selected for question 1 testrail details_3776_42
Given start scene is loaded
And question is loaded:
| object_name  |
| Stage_HKQg4m(Clone) |
And verify text lines in multiple text boxes:
| object_name | text |
| Intro1/TextTemplate | Helen is off to help advocate for the Supers. |
| Intro2/TextTemplate | Tap the correct answer. |
And verify the element:
| object_name      |
| Reference/Holder |
| Reference/PlaceHolderReferenceImage  |
| Reference/PlaceHolderReferenceImage (1) |
And verify the text: "Helen is off to help advocate for the Supers." for element: "Intro1/TextTemplate"
When select the option and verify:  
| option        | acceptable |
| CorrectOption | true       |
Then update the result to testrail
