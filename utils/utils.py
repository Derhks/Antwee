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


def small_synopsis(text: str) -> str:
    synopsis = ''

    text_split = text.split(sep='.')

    for idx in range(len(text_split)):
        if (len(synopsis) + len(text_split[idx])) < 340:
            synopsis += text_split[idx] + '.'
        else:
            break

    return synopsis
