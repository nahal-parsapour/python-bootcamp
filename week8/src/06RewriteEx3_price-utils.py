#

def convert_price_to_float(price_str):
    if not price_str:
        return 0.0
    clean = price_str.replace("£", "").replace("$","").replace(",","").strip()
    return float(clean)

def extract_titles_from_products(products):
    return [product["title"] for product in products]