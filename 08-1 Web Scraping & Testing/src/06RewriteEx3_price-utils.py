#

def convert_price_to_float(price_str):
    if not price_str or price_str == ".":
        return 0.0
    clean_price = price_str.replace("£", "").replace("$", "").replace("€", "").replace(",", "").strip()
    return float(clean_price)


def extract_titles_from_products(product_dict):
    return list(product_dict.keys())


def calculate_average_price(product_dict):
    prices_float = []
    for price_str in product_dict.values():
        price_float = convert_price_to_float(price_str)
        prices_float.append(price_float)

    avg_price = sum(prices_float) / len(prices_float) if prices_float else 0.0
    return avg_price