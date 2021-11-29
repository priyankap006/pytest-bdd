Feature: Full Retirement Age Calculator
    As a person, I want to enter my date of birth which includes, Month and Year and it will return
    when I will be able to retire, so that I can plan my lifestyle after I retire.


  Scenario: Calculate the Year of Retirement
    Given the year and month of birth "1993", "3"
    When the year of retirement is returned
    Then verify the year is equals '2060'

  Scenario: Calculate Retirement Age
    Given the year and month of birth "2020", "10"
    When the retire age is returned
    Then verify the age is equals '67'

  Scenario: Handle the year of birth that is below 1900
    Given the year and month of birth '1800', '3'
    When the year of retirement is returned
    Then the program returns an error, and it displays the user “Year must be 1900 or above”

