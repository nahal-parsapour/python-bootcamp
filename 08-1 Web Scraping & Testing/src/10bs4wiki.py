import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html.parser")

title = soup.find("h1")
if title:
    title = title.text
else:
    title = "No Title"
print("Title:", title)

first_p = soup.find("p")
if first_p:
    first_p = first_p.text
else:
    first_p = "Paragraph not found"
print("\nFirst paragraph:", first_p)

links = []
for a in soup.find_all("a", href=True):
    links.append(a["href"])

print("\nLink Count:", len(links))
print("\n 10 First Links:")
for link in links[:10]:
    print(link)


# Dollar Price

url2 = "https://www.tgju.org"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

html = requests.get(url2, headers=headers).text
soup = BeautifulSoup(html, "html.parser")

dollar_tag = soup.find("tr", {"data-market-row": "price_dollar_rl"})
price = dollar_tag.find("td", class_="nf").text.split()

print("Dollar Price:", price)