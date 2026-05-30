from behave import given, then
import requests

API_BASE_URL = "https://api.api-onepiece.com/v2"

@given("the OnePiece API is available")
def step_given_api_available(context):
    response = requests.get(f"{API_BASE_URL}/characters/en/1")
    assert response.status_code == 200

@then("the response status code should be {expected_status:d}")
def step_then_status_code(context, expected_status):
    assert context.response.status_code == expected_status, (
        f"Expected {expected_status} but got {context.response.status_code}"
    )

@then("the response body should be null")
def step_then_body_null(context):
    assert context.response.json() is None, (
        f"Expected null but got {context.response.json()}"
    )

@then("the response should contain the fields:")
def step_then_contains_fields(context):
    data = context.response.json()
    for row in context.table:
        field = row["field"]
        expected = row["value"]
        # dot-notation
        if "." in field:
            parts = field.split(".")
            actual = data[parts[0]][parts[1]]
        else:
            actual = data.get(field)
        # boolean conversion
        if expected == "true":
            expected = True
        elif expected == "false":
            expected = False
        else:
            expected = str(expected)
            actual = str(actual)
        assert actual == expected, (
            f"Field '{field}': expected '{expected}' but got '{actual}'"
        )