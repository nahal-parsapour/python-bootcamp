# ex1
import requests

def fetch_all_titles():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    posts = response.json()
    for post in posts:
        print(post['title'])

fetch_all_titles()

# ex2
def fetch_filtered_titles():
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": 1}
    response = requests.get(url, params=params)
    posts = response.json()
    for post in posts:
        print(f"\nUser1 titles: \n{post['title']}")

fetch_filtered_titles()