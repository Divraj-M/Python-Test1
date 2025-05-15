***Settings***
Library    SeleniumLibrary

***Test Cases***
Validate Radio Button
    Open the Browser with URL
    Select impressive option from 3 radio buttons
    Verify that the radio button is selected

*** Keywords ***
Open the Browser with URL
    Open Browser    https://demo.automationtesting.in/Register.html    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

Select impressive option from 3 radio buttons
    Page Should Contain Radio Button    name:radiooptions
    Sleep    5s
    Page Should Contain Checkbox    id:checkbox1
    Sleep    5s
    Select Radio Button    radiooptions    Male

Verify that the radio button is selected
    Sleep    5s
    Radio Button Should Be Set To    radiooptions    Male