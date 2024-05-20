Feature: Stori Challenge

  Background: Setup Steps
    Given Browser launched with mobile device characteristics
    And Navigate to challenge page

   Scenario: Suggestion Class
     When Enter Me in the suggestion class and selects Mexico
     And Enter Uni in the suggestion class and selects United Arab Emirates
     And Enter Uni in the suggestion class and selects United States (USA)
     Then Suggestion Class should be correctly selected

  Scenario: Dropdown
    When Select option 2 in the dropdown
    And Select option 3 in the dropdown
    Then Should be able to see the change

  Scenario: Switch Window
    When Click "Open Window" button
    And See new opened window
    Then See "30 day money back guarantee" text
    And Window should be closed if text is not found

  Scenario: Switch Tab
    When Click "Open Tab" button
    And See new opened tab and scrolls until specific button is visible
    Then Take a screenshot that includes the button and saves it with the test case name
    And Return to first window without closing the new tab

  Scenario: Switch To Alert
    When Type "Stori Card" and click Alert button
    Then Validate printed text in the alert and clicks OK
    When Type "Stori Card" and click Confirm button
    Then Validate Confirm button and clicks OK

  Scenario: Web Table
    When Collect number of courses that cost $25 and their names
    Then Print number of courses and their names
    When Collect number of courses that cost $15 and their names
    Then Print number of courses and their names

  Scenario: Web Table Fixed
    When Collect names of all the Engineer
    Then Print names of all the Engineer
    When Collect names of all the Businessman
    Then Print names of all the Businessman

  Scenario: iFrame
    When Get the text highlighted in blue in the iframe
    Then Validate printed text
