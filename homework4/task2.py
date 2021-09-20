import requests
from requests.exceptions import RequestException
from requests.models import HTTPError


def count_dots_on_i(url: str, char_search: str = 'i') -> int:
    """
    counts given letter in html by given url (by default letter i)
    in case of any network raises ValueError
    """
    try:
        res = requests.get(url).content.decode('utf-8')
    except (ConnectionError, TimeoutError, RequestException, HTTPError):
        raise ValueError('Unreachable {url})')
    return res.count(char_search)
