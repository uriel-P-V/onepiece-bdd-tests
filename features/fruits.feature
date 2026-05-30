Feature: fruits API

  Background:
    Given the OnePiece API is available

  @smoke
  Scenario: GET fruits by ID
    When I request the fruits with ID 1
    Then the response status code should be 200

  @regression
  Scenario: validate name and type
    When I request the fruits with ID 1
    Then the response should contain the fields:
      | field  | value         |
      | name   | Gum-Gum Fruit |
      | type   | Paramecia     |