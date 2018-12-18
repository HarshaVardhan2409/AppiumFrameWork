@Account_creation
Feature: Account_creation


Background: Launch the app
Given launch the app

Scenario: Verify that tapping on 'Country dropdown', it is listing different country name with their national flag icon testrail details_4012_67
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