Feature: characters API

  Background:
    Given the OnePiece API is available

  @smoke
  Scenario: GET Luffy by ID
    When I request the Luffy with ID 1
    Then the response status code should be 200

  @regression
  Scenario: Validate basic Luffy fields
    When I request the Luffy with ID 1
    Then the response should contain the fields:
      | field  | value          |
      | name   | Monkey D Luffy |
      | size   | 174cm          |
      | age    | 19 ans         |
      | bounty | 3.000.000.000  |

  @regression
  Scenario: validate crew.name and crew.is_yonko
    When I request the Luffy with ID 1
    Then the response should contain the fields:
      | field         | value                      |
      | crew.name     | The Chapeau de Paille crew |
      | crew.is_yonko | true                       |

  @regression
  Scenario: validate fruit.name
    When I request the Luffy with ID 1
    Then the response should contain the fields:
      | field          | value                       |
      | fruit.name     | Hito Hito no Mi, Nika model |
    
  @regression
  Scenario: invalid character
    When I request the Luffy with ID 9999
    Then the response status code should be 200
    And the response body should be null

 
 