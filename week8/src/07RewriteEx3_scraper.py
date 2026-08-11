from bs4 import BeautifulSoup
import requests.compat

def extract_products_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    product_items = soup.find_all("div", class_="product-item")
    products = []
    for item in product_items:
        title_tag = item.find("span", class_="product-name")
        title = title_tag.text.strip() if title_tag else "Unknown"
        price_tag = item.find("span", class_="product-price")
        price = price_tag.text.strip() if price_tag else ""
        products.append({"title": title, "price": price})
    return products
