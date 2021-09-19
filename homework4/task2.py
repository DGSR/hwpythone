import requests
from requests.exceptions import RequestException
from requests.models import HTTPError


def count_dots_on_i(url: str) -> int:
    """
    counts letter 'i' in html by given url
    in case of any network raises ValueError
    """
    try:
        res = requests.get(url)
        return res.content.decode("utf-8").count("i")
    except (ConnectionError, TimeoutError, RequestException, HTTPError):
        raise ValueError("Unreachable {url})")
