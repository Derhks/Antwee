import requests


def check_boolean_string(string: str) -> bool:
    if string == 'True':
        return True
    else:
        return False


def get(url: str) -> dict:
    try:
        response = requests.get(url=url)

    except requests.exceptions.HTTPError as Err:
        raise Err

    return response.json()
