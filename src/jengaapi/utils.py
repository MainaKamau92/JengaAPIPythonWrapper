import datetime
from json import JSONDecodeError
from pathlib import Path
from typing import Union

import requests

from .exceptions import handle_response


def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent


def prepare_request_header(signature: Union[None, str], token: str) -> dict:
    if signature:
        return {
            "Authorization": token,
            "Content-Type": "application/json",
            "signature": signature
        }
    else:
        return {
            "Authorization": token,
            "Content-Type": "application/json"
        }


def send_post_request(headers: dict, payload: dict, url: str) -> Union[dict, JSONDecodeError]:
    response = requests.post(url, json=payload, headers=headers)
    return handle_response(response)


def send_get_request(headers: dict, url: str) -> Union[dict, JSONDecodeError]:
    response = requests.get(url, headers=headers)
    return handle_response(response)


def generate_reference() -> str:
    """
    Generate a transaction reference
    Should always be a 12 digit String
    """

    a = datetime.datetime.now()
    ref = "".join(str(a).replace(" ", "").replace("-", "").split(":")[0:2])
    return ref
