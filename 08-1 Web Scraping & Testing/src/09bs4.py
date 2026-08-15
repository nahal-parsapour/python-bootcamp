# title & first product
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

title = soup.find("title").text
print("Title:", title)

first_item = soup.find("div", class_="thumbnail")
print("Item Name:", first_item.find("a", class_="title").text)
print("Price:", first_item.find("h4", class_="price").text)


links = soup.find_all("a")
for link in links[:10]:
    print(link.get("href"))

    