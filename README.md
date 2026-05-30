# onepiece-bdd-tests

![CI](https://github.com/uriel-P-V/onepiece-bdd-tests/actions/workflows/tests.yml/badge.svg)

A BDD-based test suite for the One Piece API —
demonstrates multi-feature Gherkin organization with characters, fruits and crews,
including dot-notation for nested objects, boolean field validation,
and null body handling for invalid IDs.

---

## Project Structure

```
onepiece-bdd-tests/
├── .github/
│   └── workflows/
│       └── tests.yml                  ← GitHub Actions CI
├── features/
│   ├── steps/
│   │   ├── common_steps.py            ← Shared steps across features
│   │   ├── characters_steps.py        ← Character GET step
│   │   ├── fruits_steps.py            ← Fruit GET step
│   │   └── crews_steps.py             ← Crew GET step
│   ├── environment.py                 ← Hooks and unified mock
│   ├── characters.feature             ← Luffy fields, nested crew/fruit, null body
│   ├── fruits.feature                 ← Fruit name and type validation
│   └── crews.feature                  ← Crew name, status and is_yonko validation
└── requirements.txt
```

---

## Features

- **Nested object validation** — `crew.name`, `crew.is_yonko`, `fruit.name` via dot-notation
- **Boolean validation** — `is_yonko: true` converted from Gherkin string to Python bool
- **Null body handling** — invalid ID returns 200 with null body
- **Multi-feature organization** — three independent feature files by domain
- **Single mock** — one `patch("requests.get")` dispatching by URL
- **Tag-driven execution** — `@smoke` hits real API, `@regression` fully mocked
- **GitHub Actions CI** — smoke runs first, regression only if smoke passes

---

## BDD Scenarios

```gherkin
Feature: characters API

  @regression
  Scenario: validate crew.name and crew.is_yonko
    When I request the Luffy with ID 1
    Then the response should contain the fields:
      | field         | value                      |
      | crew.name     | The Chapeau de Paille crew |
      | crew.is_yonko | true                       |

  @regression
  Scenario: invalid character
    When I request the Luffy with ID 9999
    Then the response status code should be 200
    And the response body should be null
```

---

## Mock Strategy

Single `patch("requests.get")` dispatching by URL:

```python
def unified_mock_get(url, **kwargs):
    if url == f"{API_BASE_URL}/characters/en/1":
        mock.json.return_value = MOCK_CHARACTER
    elif url == f"{API_BASE_URL}/fruits/en/1":
        mock.json.return_value = MOCK_FRUIT
    elif url == f"{API_BASE_URL}/crews/en/1":
        mock.json.return_value = MOCK_CREW
    elif url == f"{API_BASE_URL}/characters/en/9999":
        mock.json.return_value = None
```

---

## Setup

```bash
git clone https://github.com/uriel-P-V/onepiece-bdd-tests.git
cd onepiece-bdd-tests
pip install -r requirements.txt
behave
```

---

## Running Tests

```bash
# All scenarios
behave

# Smoke only — hits real One Piece API
behave --tags=smoke

# Regression only — fully mocked, no internet required
behave --tags=regression
```

---

## CI/CD Pipeline

Two dependent jobs run on every push and pull request to `main`:

```
push / PR → smoke (3 scenarios) → regression (6 scenarios)
```

If `smoke` fails, `regression` is skipped automatically.

---

## Tech Stack

- **Python 3.11+**
- **Behave** — BDD framework with Gherkin support
- **Requests** — HTTP client for API calls
- **unittest.mock** — patch, MagicMock, side_effect
- **GitHub Actions** — CI/CD pipeline

---

## Author

**Uriel Alejandro Pérez Valdovinos**  
[github.com/uriel-P-V](https://github.com/uriel-P-V) · [linkedin.com/in/uriel-pv](https://linkedin.com/in/uriel-pv)