Feature: Register functionality

    @regression @sanity
    Scenario: Validate Register
    Given is on Registration page
    When user enters un, pw and email
    And click on signup
    Then user should be registered successfully

    @regression
    Scenario: duplicate Register
    Given is on Registration page
    When user enters duplicate un, pw and email
    And click on signup1
    Then user should not be allowed to registered

    @smoke
    Scenario: duplicate Register
    Given is on Registration page
    When user enters duplicate un, pw and email
    And click on signup2
    Then user should not be allowed to registered