@Application
Feature: Application

Background: Launch the app
Given launch app with apppackage: "com.byjus.k3" appactivity: "com.byjus.k5.MainActivity"
And scene is loaded: "GameMapScreen"
And custom wait: "30"
When scroll screen with start_x: "0.9" end_x: "0.1" start_y: "0.5" end_y: "0.5" and verify element: "Building_1(Clone)/Fractions/Title"
When scroll screen with start_x: "0.5" end_x: "0.5" start_y: "0.9" end_y: "0.1" and verify element: "Building_2(Clone)/Measure/Title"
And tap and hold element: "LibraryButton/Text" for duration: "5"
And parental access: "ParentGatePanel/Question"
And scene is loaded: "Library"
And custom wait: "3"
And tap on text element: "Header" with text: "Batch 1 - V1 (Old)"
And custom wait: "3"
And tap on text element: "Text" with text: "Games"
And custom wait: "3"
And tap on text element: "Header" with text: "G3EQ38-MCQ1"

Scenario: Check the login from start scene testrail details_3830_47
Then scene is loaded: "MCQ"
And question is loaded:
| object_name  |
| G3EQ38T337_MC1_Q1(Clone) |
And verify text lines in multiple text boxes:
| object_name | text |
| Intro1/TextTemplate | The preparations for the birthday party are in full swing! |
| Question/TextTemplate | To see what happens on Anna's birthday |
When select the option and verify:  
| option        | acceptable | animation_object |
| CorrectOption | true       | CorrectOption    |