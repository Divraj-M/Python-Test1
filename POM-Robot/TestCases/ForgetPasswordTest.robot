*** Settings ***
Documentation    Test cases for the forgot password page
Library             SeleniumLibrary
Resource            ../Resources/GenericResources.robot
Resource            ../Resources/LoginResources.robot
Resource            ../Resources/ForgetPasswordResources.robot
Test Setup          Open the Browser with URL
Test Teardown       Close browser session

*** Test Cases ***
Validate Reset Password Functionality
    [Tags]    resetpasswordfunctionality
    LoginResources.Go to forgot your password page
    ForgetPasswordResources.Verify Forgot Your Password page Opens
    ForgetPasswordResources.Fill the Forgot Password Page
    ForgetPasswordResources.Verify the message

Validate Cancel Button Functionality
    [Tags]    cancelbtn
    LoginResources.Go to forgot your password page
    ForgetPasswordResources.Verify Forgot Your Password page Opens
    ForgetPasswordResources.Cancel the Reset Button
    ForgetPasswordResources.Verify that Login Page is displayed