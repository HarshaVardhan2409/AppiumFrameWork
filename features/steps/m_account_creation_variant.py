from time import sleep
import sys
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../app/'))
from onboarding import Onboarding

sys.path.append(PATH('../../generics/'))
import constants
import generics_lib

sys.path.append(PATH('./'))
from generic_steps import GenericStep

class AccountCreation(GenericStep):
    
    @step('user taps on get started button in onboarding screens')
    def tap_on_get_started_button(self):
        self.execute_steps(u'''
        When scene is loaded: "Onboarding"
        And tap on element: "Button"
        And custom wait: "3"
        ''')
        
    @step('app should open "mobile/country" screen')
    def verify_mobile_country_screen(self):
        self.execute_steps(u'''
        Then scene is loaded: "Onboarding"
        ''')
        
    @step('country field should present with mobile number field below')
    def verify_country_mobile_field(self):
        self.execute_steps(u'''
        Then verify the element:
            | object_name |
            | Dropdown |
            | MobilePanel/InputFieldPrefab |
        ''')    
        
    @step('country and value should be set to India by default')
    def verify_default_country_value(self):
        self.execute_steps(u'''
        Then verify the text: "India" for element: "Label"
        And verify the text: "+91" for element: "CountryCode"
        ''')    
    
    @step('user selects a different country from the country drop down')
    def select_different_country(self):
        self.execute_steps(u'''
        When tap on element: "arrowIndicator"
        And custom wait: "3"
        And tap on text element: "Item Label" with text: "Oman"
        ''')
        
    @step('country code gets changed automatically in mobile number field according to the newly selected country and matches it')
    def verify_changed_country_code(self):
        self.execute_steps(u'''
        Then verify the text: "+968" for element: "CountryCode"
        ''')
        
    @step('user taps on mobile number field and enters a number manually Or selects mobile number from the pop-up if there a sim added')
    def enter_mobile_number(self):
        self.execute_steps(u'''
        When tap on element: "MobilePanel/InputFieldPrefab"
        And enter the: "number": "1552009999" in element: "MobilePanel/InputFieldPrefab"
        ''')
        
    @step('switches country from the country drop down')
    def switch_country(self):
        self.execute_steps(u'''
        When tap on element: "arrowIndicator"
        And custom wait: "3"
        And tap on text element: "Item Label" with text: "Saudi Arabia"
        ''')
        
    @step('only country code should change and previous mobile number entered should remain')
    def verify_country_code(self):
        self.execute_steps(u'''
        Then verify the text: "+966" for element: "CountryCode"
        And verify the text: "1552009999" for element: "MobilePanel/InputFieldPrefab/Text"
        ''')
        
    @step('user selects india from country drop down')
    def verify_country(self):
        self.execute_steps(u'''
        When verify the text: "India" for element: "Label"
        ''') 
        
    @step('user taps on mobile number field and tries to enter less than or more than 10 digits')
    def enter_lesser_mobile_number(self):
        self.execute_steps(u'''
        When tap on element: "MobilePanel/InputFieldPrefab"
        And enter the: "number": "444455550" in element: "MobilePanel/InputFieldPrefab"
        And verify the element:
            | object_name           |
            | CountryAndEmail(Clone) |
        ''')   
        
    @step('Next button should be disabled until valid number with length is entered')
    def tap_on_nextbutton(self):
        self.execute_steps(u'''
        Then tap on element: "NextButton/Text"
        And custom wait: "2"
        And verify the element:
            | object_name           |
            | CountryAndEmail(Clone) |
        ''')    
        
    @step('user selects a different country from drop down that is not india')
    def select_different_country_in_dropdown(self):
        self.execute_steps(u'''
        When tap on element: "arrowIndicator"
        And custom wait: "3"
        And tap on text element: "Item Label" with text: "UAE"
        ''')    
        
    @step('user taps on mobile number field and enters less than 7 digits or more than 7 digits')
    def enter_less_mobile_number(self):
        self.execute_steps(u'''
        When tap on element: "MobilePanel/InputFieldPrefab"
        And enter the: "number": "444455" in element: "MobilePanel/InputFieldPrefab"
        And verify the element:
            | object_name           |
            | CountryAndEmail(Clone) |
        ''')   
        
    @step('user taps on Privacy Policy link below mobile number field')
    def tap_on_privacy_policy_link(self):
        self.execute_steps(u'''
        When tap on element: "PolicyLinkPP"
        ''')        
        
    @step('app should redirect to mobile browser and open only Privacy Policy page')
    def verify_privacy_policy_in_browser(self):
        self.execute_steps(u'''
        Then verify native app for "Privacy Policy"
        And navigate back
        ''')    
        
    @step('user taps on Terms and Conditions link below mobile number field')
    def tap_on_terms_and_condition_link(self):
        self.execute_steps(u'''
        When tap on element: "PolicyLinkTnC"
        ''')    
        
    @step('app should redirect to mobile browser and open only Terms and Conditions page')
    def verify_terms_and_condition_in_browser(self):
        self.execute_steps(u'''
        Then verify native app for "Terms & Conditions"
        ''')    
        
    @step('"Terms and Conditions" and "Privacy Policy" are displayed/highlighted as hyperlinks and capitalized below the "Next" button')
    def verify_terms_and_condition_privacy_policy_text(self):
        self.execute_steps(u'''
        Then verify the text: "By clicking next, you consent to all data practices described in the Privacy Policy and Terms & Conditions." for element: "PolicyLinkText"
        ''')    
        
    @step('user taps on mobile number field')
    def tap_on_mobile_number_field(self):
        self.execute_steps(u'''
        When tap on element: "MobilePanel/InputFieldPrefab"
        ''')    
        
    @step('user taps on country field')
    def tap_on_country_field(self):
        self.execute_steps(u'''
        When tap on element: "arrowIndicator"
        And custom wait: "3"
        ''')    
        
    @step('following list of countries with their national flag and country code for MVP should be listed: India, Bahrain, Kuwait, Oman, Qatar, Saudi Arabia, UAE')
    def verify_list_of_country_with_flag(self):
        self.execute_steps(u'''
        Then verify text lines in multiple text boxes:
            | object_name | text |
            | Dropdown/Label                  | India        |
            | Item 0: Bahrain/Item Label      | Bahrain      |
            | Item 1: UAE/Item Label          | UAE          |
            | Item 2: Kuwait/Item Label       | Kuwait       |
            | Item 3: Oman/Item Label         | Oman         |
            | Item 4: Qatar/Item Label        | Qatar        |
            | Item 5: Saudi Arabia/Item Label | Saudi Arabia |
        And verify the country a_images:
            | object_name                | image_name  |
            | Dropdown/CountryIcon       | India       |
            | Item 0: Bahrain/Image      | Bahrain     |
            | Item 1: UAE/Image          | UAE         |
            | Item 2: Kuwait/Image       | Kuwait      |
            | Item 3: Oman/Image         | Oman        |
            | Item 4: Qatar/Image        | Qatar       |
            | Item 5: Saudi Arabia/Image | SaudiArabia |
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
        ''')
    
    @step('user taps on mobile number field and enters a mobile number manually')
    def enter_existing_mobile_number(self):
        self.execute_steps(u'''
        When tap on element: "MobilePanel/InputFieldPrefab"
        And enter the: "number": "4444555502" in element: "MobilePanel/InputFieldPrefab"
        And tap on element: "NextButton"
        And verify the element:
            | object_name           |
            | OTPVerification(Clone) |
        ''')

    @step('user taps edit option in otp screen')
    def tap_on_edit_option(self):
        self.execute_steps(u'''
        When tap on element: "UserMobileText/Edit"
        And verify the element:
            | object_name           |
            | UpdateCountryAndMobileNumber(Clone) |
        ''')
    
    @step('user taps on mobile number field and tries to enter a mobile number manually')
    def update_mobile_number(self):
        self.execute_steps(u'''
        When tap on element: "MobilePanel/InputFieldPrefab"
        And enter the: "number": "4444555502" in element: "MobilePanel/InputFieldPrefab"
        ''')
    
    
    
    
    
        
           