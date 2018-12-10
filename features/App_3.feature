@Application
Feature: Application

Background: Launch the app
Given launch app with apppackage: "com.byjus.k3" appactivity: "com.byjus.k5.MainActivity"
And scene is loaded: "GameMapScreen"
And custom wait: "30"
And tap and hold element: "LibraryButton/Text" for duration: "7"
And parental access: "ParentGatePanel/Question"
And scene is loaded: "Library"
And custom wait: "3"
And tap on text element: "Header" with text: "Batch 1 - V1 (Old)"
And custom wait: "3"
And tap on text element: "Text" with text: "Games"
And custom wait: "3"
And tap on text element: "Header" with text: "G3MQ30-Match1"

Scenario: Check the login from start scene testrail details_3830_47
Then scene is loaded: "classification"
And question is loaded:
| object_name  |
| DraggableObject2degree(Clone)&DraggableObject_1Stage_1 |
And custom wait: "15"
When drag and drop the draggables to bucket and verify position:
| draggable                                               | bucket                                | acceptable |
| DraggableObject2degree(Clone)&DraggableObject_1Stage_1  | BucketSnowgies(Clone)&Bucket_1Stage_1 | true       |
| DraggableObject42degree(Clone)&DraggableObject_2Stage_1 | BucketBread(Clone)&Bucket_2Stage_1    | true       |
And question is loaded:
| object_name  |
| BucketCake(Clone)&Bucket_1Stage_2 |