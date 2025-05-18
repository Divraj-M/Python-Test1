*** Settings ***
Documentation    Test Alert Handling
Library    SeleniumLibrary
Test Teardown    Close Browser

*** Test Cases ***
Handling Alerts
    Open the browser with URL
    Handle the alert simple
    Assert the simple alert
    Handle the confirm alert
    Assert the confirm alert
    Handle the prompt alert
    Assert the prompt alert

*** Keywords ***
Open the browser with URL
    Open Browser    https://demo.automationtesting.in/Alerts.html    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5

Handle the alert simple
    Click Element    xpath://button[@class='btn btn-danger']
    
Assert the simple alert
    Alert Should Be Present    I am an alert box!    ACCEPT
    Sleep    2s

Handle the confirm alert
    Click Element    xpath://a[contains(text(),'Alert with OK & Cancel ')]
    Click Button    xpath://button[contains(text(),'click the button to display a confirm box ')]
   
Assert the confirm alert
    Alert Should Be Present    Press a Button !      
    Handle Alert    ACCEPT  
    Sleep    2s

Handle the prompt alert
    Click Element    xpath://a[contains(text(),'Alert with Textbox ')]
    Sleep    4s
    Click Button    xpath=//button[contains(text(),'click the button to demonstrate the prompt box')]
    Sleep    2s
    Input Text Into Alert    Divraj
Assert the prompt alert
    Page Should Contain    Divraj
    Sleep    2s
    

    
