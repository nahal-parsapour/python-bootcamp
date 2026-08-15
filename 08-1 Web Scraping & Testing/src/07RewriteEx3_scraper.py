from bs4 import BeautifulSoup
import requests
import requests.compat

def extract_products_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    products = soup.find_all("div", class_="product-item")

    product_dict = {}
    for item in products:
        title_tag = item.find("span", class_="product-name")
        title = title_tag.text.strip() if title_tag else "Unknown"

        price_tag = item.find("span", class_="product-price")
        price_str = price_tag.text.strip() if price_tag else "."

        product_dict[title] = price_str

    return product_dict

def extract_product_links(url="https://www.scrapingcourse.com/pagination"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("div", class_="product-item")

    product_links = []
    for product in products:
        link_tag = product.find("a") if product.find("a") else None
        if link_tag:
            href = link_tag.get("href")
            full_url = requests.compat.urljoin(url, href)
            product_links.append(full_url)
        else:
            product_links.append(None)

    return product_links