*** Settings ***
Library           SeleniumLibrary
Library           DataDriver    file=C:/Users/Lenovo/Desktop/Python-Test1/DataDriven-SauceDemo/Resources/LoginData.xlsx    sheet_name=Sheet1
Test Template     Validate successful login
Test Teardown     Close All Browsers

*** Variables ***
${browser}                chrome
${login_btn}              xpath://input[@id='login-button']
${success_message}        xpath://div[@class='product_label']
${error_message}          xpath://h3
${url}                    https://www.saucedemo.com/v1/index.html
${username}    
${password}    
${Assert}

*** Test Cases ***
Login with sauce demo using    ${username}    ${password}    ${Assert}

*** Keywords ***

Validate successful login
    [Arguments]    ${username}    ${password}    ${Assert}
    Open the browser with URL
    Fill the login Form    ${username}    ${password}
    Verify the message is correct    ${Assert}

Open the browser with URL
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Set Selenium Implicit Wait    5

Fill the login Form
    [Arguments]    ${username}    ${password}
    Input Text    css:input[name="user-name"]    ${username}
    Input Password    css:input[name="password"]    ${password}
    Click Button    ${login_btn}

Verify the message is correct
    [Arguments]    ${Assert}
    Run Keyword If    '${Assert}'=='Products'
    ...    Element Text Should Be    ${success_message}    ${Assert}
    ...    ELSE
    ...    Element Should Contain    ${error_message}    ${Assert}