# rewrite ex 01 & 02 for testt

import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout, RequestException

def fetch_titles_from_api(user_id=None):
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": user_id} if user_id else {}
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        posts = response.json()
        titles = [post['title'] for post in posts]
        return titles
    except (ConnectionError, HTTPError, Timeout, RequestException, ValueError):
        return []