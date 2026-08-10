import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout, RequestException

def fetch_titles_with_error_handling():
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": 1}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        posts = response.json()

        print(f"{len(posts)} posts found for userId=1:")
        for post in posts:
            print(f" - {post['title']}")

    except ConnectionError:
        print("Connection Error")
    except HTTPError:
        print("HTTP Error: {e.response.status_code}")
    except Timeout:
        print("Timeout Error")
    except RequestException as e:
        print("An error occured: {e}")
    except ValueError:
        print("JSON Response is not valid")

fetch_titles_with_error_handling()