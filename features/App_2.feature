@Application
Feature: Application

Background: Launch the app
Given launch app with apppackage: "com.byjus.k3" appactivity: "com.byjus.k5.MainActivity"


Scenario: Check the login from start scene testrail details_3830_47
Given  scene is loaded: "GameMapScreen"
And custom wait: "30"
When tap and hold element: "LibraryButton/Text" for duration: "5"
And parental access: "ParentGatePanel/Question"
And scene is loaded: "Library"
And custom wait: "3"
And tap on text element: "Header" with text: "Batch 1 - V1 (Old)"
And custom wait: "3"
And tap on text element: "Text" with text: "Games"
And custom wait: "3"
And tap on text element: "Header" with text: "G3EQ38-MCQ1"
Then scene is loaded: "MCQ"