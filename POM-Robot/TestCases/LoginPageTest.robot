# *** Settings ***
# Documentation       Test cases for the login page
# Library             SeleniumLibrary
# Resource            ../Resources/GenericResources.robot
# Resource            ../Resources/LoginResources.robot
# Resource            ../Resources/DashboardResources.robot
# Test Setup          Open the Browser with URL
# Test Teardown       Close browser session

# *** Test Cases ***

# Validate Unsuccessful Login using invalid credentials
#     [Tags]    logininvalidcredentials
#     LoginResources.Fill the login form    ${valid_username}    ${invalid_password}
#     LoginResources.Verify the error message is correct

# Validate Unsuccessful Login for blank username
#     [Tags]    loginwithblankusername
#     LoginResources.Fill the login form    ${blank_username}    ${valid_password}
#     LoginResources.verify the error message is displayed for username

# Validate Unsuccessful Login for blank password
#     [Tags]    loginwithblankpassword
#     LoginResources.Fill the login form    ${valid_username}    ${blank_password}
#     LoginResources.verify the error message is displayed for password

# Validate the successful login
#     [Tags]    successfulLogin
#     LoginResources.Fill the login form    ${valid_username}    ${valid_password}
#     DashboardResources.Verify Dashboard Page opens


*** Settings ***
Documentation       Test cases for the login page
Library             SeleniumLibrary
Resource            ../Resources/GenericResources.robot
Resource            ../Resources/LoginResources.robot
Resource            ../Resources/DashboardResources.robot
    
Test Setup          Open the Browser with URL
Test Teardown       Close browser session

*** Test Cases ***

Validate Unsuccessful Login using invalid credentials
    [Tags]    logininvalidcredentials
    LoginResources.Fill the login form    ${valid_username}    ${invalid_password}
    LoginResources.Verify the error message is correct

Validate Unsuccessful Login for blank username
    [Tags]    loginwithblankusername
    LoginResources.Fill the login form    ${blank_username}    ${valid_password}
    LoginResources.verify the error message is displayed for username

Validate Unsuccessful Login for blank password
    [Tags]    loginwithblankpassword
    LoginResources.Fill the login form    ${valid_username}    ${blank_password}
    LoginResources.verify the error message is displayed for password

Validate the successful login
    [Tags]    successfulLogin
    LoginResources.Fill the login form    ${valid_username}    ${valid_password}
    DashboardResources.Verify Dashboard Page opens
    