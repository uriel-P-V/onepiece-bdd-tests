from behave import when
import requests

API_BASE_URL = "https://api.api-onepiece.com/v2"

@when("I request the fruits with ID {fruit_id:d}")
def step_when_request_fruit(context, fruit_id):
    context.response = requests.get(
        f"{API_BASE_URL}/fruits/en/{fruit_id}"
    )