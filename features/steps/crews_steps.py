from behave import when
import requests

API_BASE_URL = "https://api.api-onepiece.com/v2"

@when("I request the crews with ID {crew_id:d}")
def step_when_request_crew(context, crew_id):
    context.response = requests.get(
        f"{API_BASE_URL}/crews/en/{crew_id}"
    )