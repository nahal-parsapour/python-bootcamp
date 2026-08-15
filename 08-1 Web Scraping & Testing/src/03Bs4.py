#
#
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://books.toscrape.com/"
# response = requests.get(url)
#
# soup = BeautifulSoup(response.content, "html.parser")
#
# books = soup.find_all("article", class_="product_pod")
# print(f"{len(books)} books found")
#
# book_dict = {}
# for book in books:
#     title_tag = book.find("h3").find("a")
#     title = title_tag.get("title")
#
#     price_tag = book.find("p", class_="price_color")
#     price_str = price_tag.text
#
#     book_dict[title] = price_str
#
# for title, price in list(book_dict.items())[:3]: # show first 3 items
#     print(f"{title}: {price}")

import requests
from bs4 import BeautifulSoup
import requests.compat

url = "https://www.scrapingcourse.com/pagination"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

products = soup.find_all("div", class_="product-item")
print(f"✅Number of founded products: {len(products)}")

# Create a dictionary of {title: price}
product_dict = {}
for product in products:
    title_tag = product.find("span", class_="product-name")
    title = title_tag.text.strip() if title_tag else "Unknown"

    price_tag = product.find("span", class_="product-price")
    price_str = price_tag.text.strip() if price_tag else "."

    product_dict[title] = price_str

print("\n🛍️Sample products:")
for title, price in list(product_dict.items())[:3]: # Show first 3 items
    print(f" -{title}: {price}")


# Convert prices to float and calculate average
prices_float = []

for price_str in product_dict.values():
    clean_price = price_str.replace("$", "").replace("£", "").strip()
    price_float = float(clean_price)
    prices_float.append(price_float)

avg_price = sum(prices_float) / len(prices_float) if prices_float else 0
print(f"\n📊Average price of products: {avg_price}")


# Extract all product links (href)
product_links = []
for product in products:
    link_tag = product.find("a") if product.find("a") else None
    if link_tag:
        href = link_tag.get("href")
        full_url = requests.compat.urljoin(url, href)
        product_links.append(full_url)
    else:
        product_links.append(None)

print("\n🔗️Sample Product links:")
for link in product_links[:3]:
    print(link)