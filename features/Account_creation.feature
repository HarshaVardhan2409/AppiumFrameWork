@account_creation
Feature: Account_creation

Background: Launch the app
Given launch the app


Scenario: Verify that tapping on 'Country dropdown', it is listing different country name with their national flag icon testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And tap on element: "arrowIndicator"
Then verify text lines in multiple text boxes:
| object_name                     | text     	 |
| Dropdown/Label                  | India    	 |
| Item 0: Bahrain/Item Label      | Bahrain 	 |
| Item 1: UAE/Item Label          | UAE     	 |
| Item 2: Kuwait/Item Label       | Kuwait  	 |
| Item 3: Oman/Item Label         | Oman    	 |
| Item 4: Qatar/Item Label        | Qatar        |
| Item 5: Saudi Arabia/Item Label | Saudi Arabia |
And verify the country images:
| object_name                | image_name |
| Dropdown/CountryIcon       | India      |
| Item 0: Bahrain/Image      | Bahrain 	  |
| Item 1: UAE/Image          | UAE     	  |
| Item 2: Kuwait/Image       | Kuwait  	  |
| Item 3: Oman/Image         | Oman    	  |
| Item 4: Qatar/Image        | Qatar      |
| Item 5: Saudi Arabia/Image | SaudiArabia |
And tap on element: "arrowIndicator"
And close the app


Scenario: Verify that changing country from the 'Country drop down', the country code in mobile number field gets changed automatically testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then  scene is loaded: "Onboarding"
When custom wait: "14"
And verify the country name, national flag and country code for: "India"
When tap on element: "arrowIndicator"
And tap on text element: "Item Label" with text: "Bahrain"
Then verify the country name, national flag and country code for: "Bahrain"
When tap on element: "arrowIndicator"
And tap on text element: "Item Label" with text: "UAE"
Then verify the country name, national flag and country code for: "UAE"
When tap on element: "arrowIndicator"
And tap on text element: "Item Label" with text: "Kuwait"
Then verify the country name, national flag and country code for: "Kuwait"
When tap on element: "arrowIndicator"
And tap on text element: "Item Label" with text: "Oman"
Then verify the country name, national flag and country code for: "Oman"
When tap on element: "arrowIndicator"
And tap on text element: "Item Label" with text: "Qatar"
Then verify the country name, national flag and country code for: "Qatar"
When tap on element: "arrowIndicator"
And tap on text element: "Item Label" with text: "Saudi Arabia"
Then verify the country name, national flag and country code for: "Saudi Arabia"
When tap on element: "arrowIndicator"
And tap on text element: "Item Label" with text: "India"
Then verify the country name, national flag and country code for: "India"
And close the app


Scenario: Verify that both 'Terms and Conditions' and 'Privacy Policy' both are displayed/highlighted as hyperlinks below the 'Next' button testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And tap on element: "PolicyLinkText"
And tap on element with text: "Just once"
And custom wait: "5"
Then verify native app for "Privacy Policy"
When navigate back
And navigate back
Then verify the element:
| object_name    |
| PolicyLinkText |
And close the app


Scenario: Verify that tapping on 'Next' in 'Mobile/Country' screen with all relevant data entered redirects to 'Child Profile' screen where 'Child Name' can be entered and 'Grade' can be selected testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
Then verify the element:
| object_name           |
| GradeSelection(Clone) |
And close the app


Scenario: Verify that 'Child Name' field does not allow any spaces at the start/end/middle of the name testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
And enter the: "nick name": " ji mm y " in element: "GradeSelection(Clone)/Background/InputFieldPrefab"
Then verify the text: "jimmy" for element: "GradeSelection(Clone)/Background/InputFieldPrefab/Text"
And close the app


Scenario: Verify the 'Grades' testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
And enter the: "nick name": "jimmy" in element: "GradeSelection(Clone)/Background/InputFieldPrefab"
Then verify text lines in multiple text boxes for object with same names:
| object_name | text       |
| Text        | Pre School |
| Text        | Pre-K  	   |
| Text        | KG         |
| Text        | Grade 1    |
| Text        | Grade 2    |
| Text        | Grade 3	   |
And close the app


Scenario: Verify that the 'Next' button is disabled until the 'Child Name' is entered and the 'Grade' has been chosen. testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
Then verify the element:
| object_name           |
| GradeSelection(Clone) |
When tap on element: "NextButton/Text"
And custom wait: "2"
Then verify the element:
| object_name           |
| GradeSelection(Clone) |
And close the app


Scenario: Verify that tapping on 'Back' button at top left of 'Child Profile' screen returns player to 'Mobile/Country' screen where all fields can be modified testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And tap on element: "arrowIndicator"
And tap on text element: "Item Label" with text: "Bahrain"
Then verify the country name, national flag and country code for: "Bahrain"
And enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
Then verify the element:
| object_name           |
| GradeSelection(Clone) |
When tap on element: "BackButton"
Then verify the element:
| object_name           |
| CountryAndEmail(Clone) |
When tap on element: "arrowIndicator"
And tap on text element: "Item Label" with text: "India"
Then verify the country name, national flag and country code for: "India"
When clear text field: "InputFieldPrefab/Text"
And enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
Then verify the element:
| object_name           |
| GradeSelection(Clone) |
And close the app


Scenario: Verify that tapping on 'Next' button in 'Child Profile' screen redirects player to OTP Verification' screen testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
And enter the: "nick name": "jimmy" in element: "GradeSelection(Clone)/Background/InputFieldPrefab"
And tap on text element: "Text" with text: "Pre School"
And tap on element: "NextButton"
Then verify the element:
| object_name            |
| OTPVerification(Clone) |
And verify the text: "Resend" for element: "Resend Code"
And close the app


Scenario: Verify that tapping on 'Edit' button redirects player to 'Mobile/Country' screen where both mobile number and country can be edited, and Next button is replaced with Update button. testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And tap on element: "arrowIndicator"
And tap on text element: "Item Label" with text: "Bahrain"
Then verify the country name, national flag and country code for: "Bahrain"
When enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
Then verify the element:
| object_name           |
| GradeSelection(Clone) |
When enter the: "nick name": "jimmy" in element: "GradeSelection(Clone)/Background/InputFieldPrefab"
And tap on text element: "Text" with text: "Pre School"
And tap on element: "NextButton"
Then verify the element:
| object_name            |
| OTPVerification(Clone) |
When tap on element: "Edit/Text"
Then verify the element:
| object_name            |
| UpdateCountryAndMobileNumber(Clone) |
And verify the text: "Update" for element: "NextButton/Text"
When tap on element: "arrowIndicator"
And tap on text element: "Item Label" with text: "India"
Then verify the country name, national flag and country code for: "India"
When clear text field: "InputFieldPrefab/Text"
And enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
Then verify the element:
| object_name           |
| GradeSelection(Clone) |
And close the app


Scenario: Verify that if the number entered belongs to an existing account, details entered before are scrapped and app proceeds to 'OTP Verification' screen testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And enter the: "different mobile number": "1552021559" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
And enter the: "nick name": "jimmy" in element: "GradeSelection(Clone)/Background/InputFieldPrefab"
And tap on text element: "Text" with text: "Pre School"
And tap on element: "NextButton"
Then verify the element:
| object_name            |
| OTPVerification(Clone) |
And close the app
When launch the app
And scene is loaded: "OnboardingIntroScene"
And tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And enter the: "same mobile number": "1552021559" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
Then verify the element:
| object_name            |
| OTPVerification(Clone) |
And close the app


Scenario: Verify that appropriate warning message is shown on entering incorrect OTP testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
And enter the: "nick name": "jimmy" in element: "GradeSelection(Clone)/Background/InputFieldPrefab"
And tap on text element: "Text" with text: "Pre School"
And tap on element: "NextButton"
Then verify the element:
| object_name            |
| OTPVerification(Clone) |
When enter the: "otp": "7894" in element: "InputFieldPrefab"
And custom wait: "1"
Then verify the text: "Please enter correct OTP" for element: "WrongOTPText"
And close the app


Scenario: Verify that text 'Too many attempt. Please try again later' is seen if a maximum of 3 (?) incorrect attempts in a session is made (Resend button to be disabled as per UI?) testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
And enter the: "nick name": "jimmy" in element: "GradeSelection(Clone)/Background/InputFieldPrefab"
And tap on text element: "Text" with text: "Pre School"
And tap on element: "NextButton"
Then verify the element:
| object_name            |
| OTPVerification(Clone) |
When enter the: "otp": "7894" in element: "InputFieldPrefab"
And clear text field: "InputFieldPrefab/Text"
And enter the: "otp": "3256" in element: "InputFieldPrefab"
And clear text field: "InputFieldPrefab/Text"
And enter the: "otp": "1452" in element: "InputFieldPrefab"
And verify the text: "Too many attempts.Please wait for 5 seconds" for element: "WrongOTPText"
And close the app


Scenario: Verify that tapping on 'Next' button in 'OTP Verification' screen redirects to 'Parent Profile' screen testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
And enter the: "nick name": "jimmy" in element: "GradeSelection(Clone)/Background/InputFieldPrefab"
And tap on text element: "Text" with text: "Pre School"
And tap on element: "NextButton"
Then verify the element:
| object_name            |
| OTPVerification(Clone) |
When enter the: "otp": "1234" in element: "InputFieldPrefab"
Then verify the element:
| object_name             |
| LocationAndEmail(Clone) |
And close the app


Scenario: Verify that entering 3 letters into the box returns appropriate results in the drop down for selection testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
And enter the: "nick name": "jimmy" in element: "GradeSelection(Clone)/Background/InputFieldPrefab"
And tap on text element: "Text" with text: "Pre School"
And tap on element: "NextButton"
Then verify the element:
| object_name            |
| OTPVerification(Clone) |
When enter the: "otp": "1234" in element: "InputFieldPrefab"
Then verify the element:
| object_name             |
| LocationAndEmail(Clone) |
And tap on element: "LocationPanel/InputField"
And tap on element with text: "Allow"
And enter the: "location": "Beng" in element: "LocationPanel/InputField"
Then verify the element:
| object_name               |
| LocationSuggestion(Clone) |
And close the app


@smoke
Scenario: Verify that tapping on the displayed suggestion fills it into the text box and selecting 'Add account' navigates to add account screen testrail details_3830_47
Given scene is loaded: "OnboardingIntroScene"
When tap on element: "Button"
Then scene is loaded: "Onboarding"
When custom wait: "14"
And enter the: "different mobile number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
And tap on element: "NextButton"
And enter the: "nick name": "jimmy" in element: "GradeSelection(Clone)/Background/InputFieldPrefab"
And tap on text element: "Text" with text: "Pre School"
And tap on element: "NextButton"
Then verify the element:
| object_name            |
| OTPVerification(Clone) |
When enter the: "otp": "1234" in element: "InputFieldPrefab"
Then verify the element:
| object_name             |
| LocationAndEmail(Clone) |
And tap on element: "LocationPanel/InputField"
And tap on element with text: "Allow"
And enter the: "location": "Beng" in element: "LocationPanel/InputField"
Then verify the element:
| object_name               |
| LocationSuggestion(Clone) |
When tap on text element: "Text" with text: "Bengaluru"
And tap on element: "EmailPanel/InputFieldPrefab"
And tap on element with text: "Add account"
And tap on element with text: "OK"
Then verify native app for "Next"
When navigate back
And tap on element with text: "@"
And tap on element with text: "OK"
And tap on element: "NextButton"
Then verify the element:
| object_name                |
| OnBoardingCompleted(Clone) |
And custom wait: "3"
And tap on element: "NextButton"
Then scene is loaded: "GameMapScreen"
And custom wait: "30"
And tap on element: "Avatar(Clone)"
And tap on element: "LetsStartButton"
Then custom wait: "30"
And scene is loaded: "GameMapScreen"
And close the app
