***Settings***
Library    SeleniumLibrary
***Test Cases***
Login with correct Username and Password
    Open Browser    https://the-internet.herokuapp.com/login    edge
    Input Text    id:username    tomsmith
    Input Text    id:password    SuperSecretPassword!
    Click Button    class:radius
    Element Should Contain    id:flash    You logged into a secure area!
    Close Browser
