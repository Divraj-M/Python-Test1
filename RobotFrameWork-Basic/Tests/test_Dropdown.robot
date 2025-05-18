*** Settings ***
Documentation    Test Dropdown Selection
Library           SeleniumLibrary
Test Teardown    Close All Browsers




*** Test Cases ***
Select options in Dropdown
    Open the browser with URL
    Select the dropdown option APIs by value
    Select the dropdown option Microsoft by index
    Select the dropdown option CSS by label

    

*** Keywords ***
Open the browser with URL
    Open Browser    https://demo.automationtesting.in/Register.html    chrome
    Maximize Browser Window 
    Set Selenium Implicit Wait    5

Select the dropdown option APIs by value
    Select From List By Value    id=Skills    APIs

Select the dropdown option Microsoft by index
    Select From List By Index    id=Skills    43

Select the dropdown option CSS by label
    Select From List By Label    id=Skills    CSS