# 1. ex from copilot
import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    for p in posts[:10]:
        print(p["title"])
else: print("Error while fetching data")

# 2. create new post
data = {
    "title": "My Test Post",
    "body": "This is a test",
    "userId": 1
}
response = requests.post(url, json=data)
print("\n", response.json())

# 3. error
url = "https://jsonplaceholder.typicode.com/WRONG_URL"
response = requests.get(url)

if response.status_code != 200:
    print("\nUnsuccessful request:", response.status_code)