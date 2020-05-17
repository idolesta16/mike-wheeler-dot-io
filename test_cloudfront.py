"""
Tests the responses that come back from different variations of my personal site's URL.

Written by Michael Wheeler.
"""

import requests
from requests.exceptions import ConnectionError

PLAIN_URLS = [
    "michaelwheeler.io",
    "mikewheeler.io",
]

HTTPS_URLS = [
    "https://michaelwheeler.io",
    "https://www.michaelwheeler.io",
    "https://mikewheeler.io",
    "https://www.mikewheeler.io",
]

HTTP_URLS = [
    "http://michaelwheeler.io",
    "http://www.michaelwheeler.io",
    "http://mikewheeler.io",
    "http://www.mikewheeler.io",
]


def test_request(url):
    try:
        r = requests.get(url)
        print(f'{url} -> {r.status_code}')
    except ConnectionError as e:
        print(f'{url} -> ERROR: {type(e).__name__}')
        print(f'\t{e.args}')


for url in HTTPS_URLS + HTTP_URLS:
    test_request(url)
    test_request(url + "/")
