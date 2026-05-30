Feature: crews API

  Background:
    Given the OnePiece API is available

  @smoke
  Scenario: GET crews by ID
    When I request the crews with ID 1
    Then the response status code should be 200

  @regression
  Scenario: validate name, status, is_yonko
    When I request the crews with ID 1
    Then the response should contain the fields:
      | field   | value                      |
      | name    | The Chapeau de Paille crew |
      | status  | assets                     |
      | is_yonko| true                       |