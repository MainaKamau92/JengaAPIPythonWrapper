from pathlib import Path
from json import JSONDecodeError
from typing import Union

import requests
from .exceptions import handle_response


def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent


def prepare_request_header(signature: str, token: str) -> dict:
    return {
        "Authorization": token,
        "Content-Type": "application/json",
        "signature": signature
    }


def send_post_request(headers: dict, payload: dict, url: str) -> Union[dict, JSONDecodeError]:
    response = requests.post(url, json=payload, headers=headers)
    return handle_response(response)


def send_get_request(headers: dict, url: str) -> Union[dict, JSONDecodeError]:
    response = requests.get(url, headers=headers)
    return handle_response(response)
