***Settings***
Library    SeleniumLibrary

***Test Cases***
Search the Selenium keyword in the Browser
    Open Browser    https://www.google.com    browser=chrome
    Set Selenium Implicit Wait    5
    Maximize Browser Window
    Input Text    name=q    Selenium
    Press Key    name=q    \\13
    # pages should contain    Selenium
    Close Browser
