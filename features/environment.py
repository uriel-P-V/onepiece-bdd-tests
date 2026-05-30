from unittest.mock import patch, MagicMock

API_BASE_URL = "https://api.api-onepiece.com/v2"

MOCK_CHARACTER = {
    "id": 1,
    "name": "Monkey D Luffy",
    "size": "174cm",
    "age": "19 ans",
    "bounty": "3.000.000.000",
    "crew": {
        "name": "The Chapeau de Paille crew",
        "is_yonko": True
    },
    "fruit": {
        "name": "Hito Hito no Mi, Nika model"
    }
}

MOCK_FRUIT = {
    "id": 1,
    "name": "Gum-Gum Fruit",
    "type": "Paramecia"
}

MOCK_CREW = {
    "id": 1,
    "name": "The Chapeau de Paille crew",
    "status": "assets",
    "is_yonko": True
}


def unified_mock_get(url, **kwargs):
    mock = MagicMock()

    if url == f"{API_BASE_URL}/characters/en/1":
        mock.status_code = 200
        mock.json.return_value = MOCK_CHARACTER

    elif url == f"{API_BASE_URL}/fruits/en/1":
        mock.status_code = 200
        mock.json.return_value = MOCK_FRUIT


    elif url == f"{API_BASE_URL}/crews/en/1":
        mock.status_code = 200
        mock.json.return_value = MOCK_CREW

    elif url == f"{API_BASE_URL}/characters/en/9999":
        mock.status_code = 200
        mock.json.return_value = None

    return mock


def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")

    if "regression" in scenario.tags:
        context.mock_get = patch("requests.get", side_effect=unified_mock_get)
        context.mock_get.start()


def after_scenario(context, scenario):
    print( f"Finished scenario: " f"{scenario.name} - Status: {scenario.status}")

    if "regression" in scenario.tags:
        context.mock_get.stop()