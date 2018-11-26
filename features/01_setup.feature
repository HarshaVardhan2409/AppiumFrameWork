@App_setup
Feature: App_setup

Background: Launch the app
Given launch the app

Scenario: Check the login from start scene testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
And scene is loaded: "Onboarding"
And custom wait: "15"
And enter the: "mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
And enter the: "nick name": "jimmy" in element: "GradeSelection(Clone)/Background/InputFieldPrefab"
And tap on text element: "Text" with text: "Pre School"
And tap on element: "NextButton"
And enter the: "otp": "1234" in element: "OTPVerification(Clone)/Background/InputFieldPrefab"
And tap on element: "LocationPanel/InputField"
And tap on element with text: "Allow"
And enter the: "location": "Benguet" in element: "LocationPanel/InputField"
And custom wait: "3"
And tap on text element: "Text" with text: "Benguet"
And tap on element: "EmailPanel/InputFieldPrefab"
And custom wait: "3"
And tap on element with text: "cbtcrowd601@gmail.com"
And tap on element with text: "OK"
And tap on element: "NextButton"
And custom wait: "6"
And tap on element: "NextButton"
Then scene is loaded: "GameMapScreen"
And custom wait: "30"
And tap on element: "Avatar(Clone)"
And tap on element: "LetsStartButton"
Then custom wait: "30"
And scene is loaded: "GameMapScreen"
